# all-the-german-words

An array of ~1,648,000 German words derived from [Wiktionary](https://de.wiktionary.org/) and [the Letterpress word
list](https://github.com/atebits/Words).
Provides normal case, lowercase and uppercase versions.
Works with node and browserify.

Try also the original [an-array-of-english-words](http://npm.im/an-array-of-english-words) from [zeke](https://github.com/zeke/).

## Programmatic Usage

To use the module in Javascript code, install it locally:

```sh
npm install all-the-german-words --save
```

Then:

```js
var woerter = require("all-the-german-words")
var quatschWoerter = woerter.filter(function(w) { return /quatsch/i.test(w) })
console.log(quatschWoerter)
```

## Command Line Usage

There's a CLI that prints all words to STDOUT. Install it globally:

```sh
npm i -g all-the-german-words
```

Now you can print all words:

```sh
woerter | grep Donaudampfschifffahrtsgesellschaft
```

## See also

The lowercase ascii version of this word list: [all-the-german-words-ascii](http://npm.im/all-the-german-words-ascii)