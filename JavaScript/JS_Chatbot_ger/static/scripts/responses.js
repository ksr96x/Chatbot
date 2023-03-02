//for german use nlpjsLangDe
const { StemmerDe, StopwordsDe } = nlpjsLangDe
var stemmer = new nlpjsLangDe.StemmerDe();
var stopwords = new nlpjsLangDe.StopwordsDe();

//for english use nlpjsLangEn
/*const { StemmerEn, StopwordsEn } = nlpjsLangEn
var stemmer = new StemmerEn();
var stopwords = new StopwordsEn();
*/

stopwords.dictionary = {};
stopwords.build(['ist', 'dein', 'ich', 'bin', 'falls', 'das']);

var pairs = {
  "name": "Corpus",
  "locale": "de-DE",
  "data": [
    
    {
      "intent": "agent.canyouhelp",
      "utterances": [
        "hilfe",
        "beratung"
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
      "answers": [
        "In der Tat bin ich ein Roboter. Ich werde Ihnen helfen sobald Sie mich benötigen."
      ]
    },
    {
      "intent": "greetings.bye",
      "utterances": [
        "tschüss",
        "auf wiedersehen",
        "ciao"
      ],
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
      "answers": [
        "Hallo!"
      ]
    },
    {
      "intent": "user.testing",
      "utterances": [
        "test",
        "testing",
        "testing chatbot",
        "das ist ein test",
        "ich teste dich einfach nur"
      ],
      "answers": [
        "Ich mag es getestet zu werden."
      ]
    },
  ]
}

//normalize -> tokenize -> stem -> removeStopwords
//searches in pairs if input is included | pairs = dic -> array -> dic -> array { [ { [ ] } ] }
function getBotResponse(input){
  if (input.length < 3) {return "Könnten Sie eine längere Eingabe tätigen?";}
  
  let tokAndStem = stemmer?.tokenizeAndStem(input);
  let final = stopwords?.removeStopwords(tokAndStem)
  console.log(final)
  for (let i = 0; i < pairs?.data.length; i++) {
    for (let j = 0; j < pairs.data[i].utterances.length; j++) {
      let arr = pairs.data[i].utterances[j].split(' ');
      let found = arr.some((item) => final.includes(item));
      if (found) {
        return pairs.data[i].answers.toString();
      } 
    }
  }
  return "Könnten Sie die Eingabe anders formulieren?"; 
}

/*const input = 'i am wondering if testing your developer is needed';
const input2 = '     CAN YOU ASSIST ME';
console.log(getBotResponse(input));
console.log(getBotResponse(input2));
*/


// window.getBotResponse = getBotResponse;


//Deutsche Variante (German Version)
/*const { StemmerDe, StopwordsDe } = require('@nlpjs/lang-de');
const stemmer = new StemmerDe();
const stopwords = new StopwordsDe();
stopwords.dictionary = {};
stopwords.build(['ich', 'ob', 'sie']);
*/

//stemmer.stopwords = new StopwordsDe();

/*const input = 'ich würde gerne wissen ob sie einen tester oder entwickler benötigen und wer ihr entwickler ist';
const result = stemmer.tokenizeAndStem(input);
console.log(result);*/


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