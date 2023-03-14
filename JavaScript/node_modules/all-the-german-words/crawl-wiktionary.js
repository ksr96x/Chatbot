const WikiQuery = require('./mediawiki-query')
const Q = require('q')

const wiktionary = new WikiQuery('https://de.wiktionary.org/w/api.php')

const mainGermanCategories = [
  'Kategorie:Pronomen (Deutsch)',
  'Kategorie:Präposition (Deutsch)',
  'Kategorie:Verb (Deutsch)',
  'Kategorie:Partizip (Deutsch)',
  'Kategorie:Kardinalzahl (Deutsch)',
  'Kategorie:Interjektion (Deutsch)',
  'Kategorie:Artikel (Deutsch)',
  'Kategorie:Adverb (Deutsch)',
  'Kategorie:Adjektiv (Deutsch)',
  'Kategorie:Substantiv (Deutsch)',
  'Kategorie:Wortverbindung (Deutsch)'
]

function listCategoriesRecursive (categories) {
  return Q.all(categories.map(listCategoryRecursive)).progress(x => x.value)
}

function listCategoryRecursive (category) {
  const options = {
    generator: 'categorymembers',
    gcmlimit: 500,
    gcmtype: 'subcat',
    gcmtitle: category
  }
  return Q.Promise((resolve, reject, notify) => {
    var promise = Q()
    wiktionary.query(options)
            .progress(pages => { promise = promise.thenResolve(listCategoriesRecursive(pages.map(page => page.title)).progress(notify)) })
            .tap(() => notify(category)).then(() => promise).then(resolve, reject)
  })
}

function listGermanWordsCategories () {
  var allCategories = []
  return listCategoriesRecursive(mainGermanCategories)
        .progress(category => allCategories.push(category))
        .thenResolve(allCategories)
}

function filterAllPagesByCategories (categories) {
  const options = {
    generator: 'allpages',
    gapnamespace: 0,
    gaplimit: 500,
    prop: 'categories',
    cllimit: 500,
    clcategories: categories.join('|')
  }
  return wiktionary.query(options)
        .progress(pages => pages.filter(page => page.categories))
}

function isLegalWord (word) {
  if (/^-|-$/.test(word)) {
    return false
  }
  return true
}

listGermanWordsCategories()
    .then(cats => filterAllPagesByCategories(cats)
        .progress(pages => pages.map(page => page.title).filter(isLegalWord).forEach(word => process.stdout.write(`${word}\n`))))
    .done()
