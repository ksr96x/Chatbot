const { StemmerDe, StopwordsDe } = nlpjsLangDe
var stemmer = new nlpjsLangDe.StemmerDe();
var stopwords = new nlpjsLangDe.StopwordsDe();

stopwords.dictionary = {};
stopwords.build(["a","ab","aber","ach","acht","achte","achten","achter","achtes","ag","alle","allein","allem","allen","aller",
"allerdings","alles","allgemeinen","als","also","am","an","ander","andere","anderem","anderen","anderer","anderes","anderm",
"andern","anderr","anders","au","auch","auf","aus","ausser","ausserdem","außer","außerdem","b","bald","bei","beide","beiden",
"beim","beispiel","bekannt","bereits","besonders","besser","besten","bin","bis","bisher","bist","c","d","d.h","da","dabei",
"dadurch","dafür","dagegen","daher","dahin","dahinter","damals","damit","danach","daneben","dank","dann","daran","darauf",
"daraus","darf","darfst","darin","darum","darunter","darüber","das","dasein","daselbst","dass","dasselbe","davon","davor",
"dazu","dazwischen","daß","dein","deine","deinem","deinen","deiner","deines","dem","dementsprechend","demgegenüber","demgemäss",
"demgemäß","demselben","demzufolge","den","denen","denn","denselben","der","deren","derer","derjenige","derjenigen","dermassen",
"dermaßen","derselbe","derselben","des","deshalb","desselben","dessen","deswegen","dich","die","diejenige","diejenigen","dies",
"diese","dieselbe","dieselben","diesem","diesen","dieser","dieses","dir","doch","dort","drei","drin","dritte","dritten","dritter",
"drittes","du","durch","durchaus","durfte","durften","dürfen","dürft","e","eben","ebenso","ehrlich","ei","ei,","eigen","eigene",
"eigenen","eigener","eigenes","ein","einander","eine","einem","einen","einer","eines","einig","einige","einigem","einigen",
"einiger","einiges","einmal","eins","elf","en","ende","endlich","entweder","er","ernst","erst","erste","ersten","erster","erstes",
"es","etwa","etwas","euch","euer","eure","eurem","euren","eurer","eures","f","folgende","früher","fünf","fünfte","fünften",
"fünfter","fünftes","für","g","gab","ganz","ganze","ganzen","ganzer","ganzes","gar","gedurft","gegen","gegenüber","gehabt",
"gehen","geht","gekannt","gekonnt","gemacht","gemocht","gemusst","genug","gerade","gern","gesagt","geschweige","gewesen",
"gewollt","geworden","gibt","ging","gleich","gott","gross","grosse","grossen","grosser","grosses","groß","große","großen",
"großer","großes","gut","gute","guter","gutes","h","hab","habe","haben","habt","hast","hat","hatte","hatten","hattest","hattet",
"heisst","her","heute","hier","hin","hinter","hoch","hätte","hätten","i","ich","ihm","ihn","ihnen","ihr","ihre","ihrem","ihren",
"ihrer","ihres","im","immer","in","indem","infolgedessen","ins","irgend","ist","j","ja","jahr","jahre","jahren","je","jede",
"jedem","jeden","jeder","jedermann","jedermanns","jedes","jedoch","jemand","jemandem","jemanden","jene","jenem","jenen","jener",
"jenes","jetzt","k","kam","kann","kannst","kaum","kein","keine","keinem","keinen","keiner","keines","kleine","kleinen","kleiner",
"kleines","kommen","kommt","konnte","konnten","kurz","können","könnt","könnte","l","lang","lange","leicht","leide","lieber",
"los","m","machen","macht","machte","mag","magst","mahn","mal","man","manche","manchem","manchen","mancher","manches","mann",
"mehr","mein","meine","meinem","meinen","meiner","meines","mensch","menschen","mich","mir","mit","mittel","mochte","mochten",
"morgen","muss","musst","musste","mussten","muß","mußt","möchte","mögen","möglich","mögt","müssen","müsst","müßt","n","na",
"nach","nachdem","nahm","natürlich","neben","nein","neue","neuen","neun","neunte","neunten","neunter","neuntes","nicht",
"nichts","nie","niemand","niemandem","niemanden","noch","nun","nur","o","ob","oben","oder","offen","oft","ohne","ordnung",
"p","q","r","recht","rechte","rechten","rechter","rechtes","richtig","rund","s","sa","sache","sagt","sagte","sah","satt",
"schlecht","schluss","schon","sechs","sechste","sechsten","sechster","sechstes","sehr","sei","seid","seien","sein","seine",
"seinem","seinen","seiner","seines","seit","seitdem","selbst","sich","sie","sieben","siebente","siebenten","siebenter",
"siebentes","sind","so","solang","solche","solchem","solchen","solcher","solches","soll","sollen","sollst","sollt","sollte",
"sollten","sondern","sonst","soweit","sowie","später","startseite","statt","steht","suche","t","tag","tage","tagen","tat",
"teil","tel","tritt","trotzdem","tun","u","uhr","um","und","uns","unse","unsem","unsen","unser","unsere","unserer","unses",
"unter","v","vergangenen","viel","viele","vielem","vielen","vielleicht","vier","vierte","vierten","vierter","viertes","vom",
"von","vor","w","wahr","wann","war","waren","warst","wart","warum","was","weg","wegen","weil","weit","weiter","weitere",
"weiteren","weiteres","welche","welchem","welchen","welcher","welches","wem","wen","wenig","wenige","weniger","weniges",
"wenigstens","wenn","wer","werde","werden","werdet","weshalb","wessen","wie","wieder","wieso","will","willst","wir","wird",
"wirklich","wirst","wissen","wo","woher","wohin","wohl","wollen","wollt","wollte","wollten","worden","wurde","wurden","während",
"währenddem","währenddessen","wäre","würde","würden","x","y","z","z.b","zehn","zehnte","zehnten","zehnter","zehntes","zeit",
"zu","zuerst","zugleich","zum","zunächst","zur","zurück","zusammen","zwanzig","zwar","zwei","zweite","zweiten","zweiter",
"zweites","zwischen","zwölf","über","überhaupt","übrigens"]);

var pairs = {
  "name": "Corpus",
  "locale": "de-DE",
  "data": [
    
    {
      "intent": "agent.canyouhelp",
      "utterances": [
        "hilfe",
        "beratung",
        "steuerberatung",
        "steuererklärung machen",
        "wie sind die öffnungszeiten"
      ],
      "synonyms": [
        ["assistenz", "hilfeleistung", "unterstützung"],
        ["rat", "beratungsgespräch", "konsultation"],
        ["steuerberater", "steuerexperte", "fachkraft für steuern"],
        ["steuerformular", "jahresabschluss", "steuerliche erklärung"],
        ["geschäftszeiten", "arbeitszeiten"]
    ],
      "answers": [
        "Ich werde Ihnen sehr gerne helfen."
      ]
    },
    {
      "intent": "agent.chatbot",
      "utterances": [
        "bot",
        "chatbot",
        "robot"
      ],
      "synonyms": [],
      "answers": [
        "In der Tat bin ich ein Roboter. Ich werde Ihnen helfen sobald Sie mich benötigen."
      ]
    },
    {
      "intent": "agent.status",
      "utterances": [
        "wie gehts?",
        "wie gehts dir?",
        "wie gehts denn so?"
      ],
      "synonyms": [],
      "answers": [
        "Gut und Ihnen?"
      ]
    },
    {
      "intent": "greetings.bye",
      "utterances": [
        "tschüss",
        "auf wiedersehen",
        "ciao"
      ],
      "synonyms": [],
      "answers": [
        "Bis zum nächsten Mal."
      ]
    },
    {
      "intent": "greetings.hello",
      "utterances": [
        "hallo",
        "hi"
      ],
      "synonyms": [],
      "answers": [
        "Hallo!"
      ]
    },
    {
      "intent": "user.testing",
      "utterances": [
        "test",
        "testing",
        "das ist ein test",
        "ich teste dich einfach nur"
      ],
      "synonyms": [],
      "answers": [
        "Ich mag es getestet zu werden."
      ]
    },
    {
      "intent": "user.link",
      "utterances": [
        "testing chatbot",
        "website",
        "steuererklärung erstellen"
      ],
      "synonyms": [],
      "answers": [
        hyperlink("Besuchen Sie dazu: ", "https://www.google.com")
      ]
    },
  ]
}


function hyperlink(text, website){
  let course = website;

  let link = `<a href='${course}' target='_blank'>${course}</a>`;
  
  responseText = `${text} ${link}`;
  
  return responseText;
}

/*var arraysMatch = function (arr1, arr2) {
	if (arr1.length !== arr2.length) return false;

  arr1.sort();
  arr2.sort();
	
	for (var i = 0; i < arr1.length; i++) {
		if (arr1[i] !== arr2[i]) return false;
	}

	return true;

};*/

function arraysMatch(arr1, arr2) {
  if (arr1.length !== arr2.length) return false;

  const sortedArr1 = arr1.slice().sort();
  const sortedArr2 = arr2.slice().sort();

  for (let i = 0; i < sortedArr1.length; i++) {
      if (sortedArr1[i] !== sortedArr2[i]) return false;
  }

  return true;
}

function score(arr1, arr2) {
  let matchedWords = 0;
  for (let i = 0; i < arr2.length; i++) {
    if (arr1.includes(arr2[i])) {
      matchedWords++;
    }
  }
  let score = matchedWords / arr2.length;
  console.log(score);
  return score;
}

//normalize -> tokenize -> stem -> removeStopwords
//searches in pairs if input is included | pairs = dic -> array -> dic -> array { [ { [ ] } ] }
function getBotResponse(input){
  if (input.length < 3) {return "Bitte tätigen sie eine längere Eingabe."}
  
  let tokAndStem = stemmer?.tokenizeAndStem(input);
  let final = stopwords?.removeStopwords(tokAndStem)
  console.log(final)
  for (let i = 0; i < pairs?.data.length; i++) {
    for (let j = 0; j < pairs.data[i].utterances.length; j++) {
      let arr = stemmer.stem(pairs.data[i].utterances[j].split(' '));
      var found = arr.some((item) => final.includes(item));
      var score_value = score(arr, final);
      
      if (arraysMatch(arr, final)) return pairs.data[i].answers.toString();
      
    }
    console.log(score_value);

    if (score_value > 0.6) return pairs.data[i].answers.toString()

    else if (found) return pairs.data[i].answers.toString();

     
  }
  return "Könnten Sie die Eingabe anders formulieren?"; 
}


/* sentiment analysis
const { Container } = require('@nlpjs/core');
const { SentimentAnalyzer } = require('@nlpjs/sentiment');
const { LangDe } = require('@nlpjs/lang-de');

(async () => {
const container = new Container();
container.use(LangDe);
const sentiment = new SentimentAnalyzer({ container });
const result = await sentiment.process({ locale: 'de', text: 'Ich liebe Katzen'});
console.log(result.sentiment);
})();*/

