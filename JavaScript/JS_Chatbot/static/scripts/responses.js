const { StemmerEn, StopwordsEn } = require('@nlpjs/lang-en');
const stemmer = new StemmerEn();
const stopwords = new StopwordsEn();

var _ = require('underscore');

stopwords.dictionary = {};
stopwords.build(['is', 'your', 'i', 'am', 'if']);

var pairs = {
  "name": "Corpus",
  "locale": "de-DE",
  "data": [
    
    {
      "intent": "agent.canyouhelp",
      "utterances": [
        "can you help me now",
        "I need you to do something for me",
        "assist me",
        "I need you to help me",
        "can you assist me",
        "you can help me"
      ],
      "answers": [
        "I'll certainly try my best",
        "Never too busy for you. Shall we chat?",
        "Sure. I'd be happy to. What's up?",
        "I'm glad to help. What can I do for you?"
      ]
    },
    {
      "intent": "agent.chatbot",
      "utterances": [
        "are you a bot",
        "are you a chatbot",
        "you are a robot",
        "are you a program",
        "you are just a robot",
        "you are just a chatbot"
      ],
      "answers": [
        "Indeed I am. I'll be here whenever you need me"
      ]
    },
    {
      "intent": "appraisal.good",
      "utterances": [
        "that's good",
        "good to know",
        "glad to hear that",
        "really well",
        "that's awesome thank you"
      ],
      "answers": [
        "Agree!",
        "Glad you think so"
      ]
    },
    {
      "intent": "appraisal.thankyou",
      "utterances": [
        "thank you",
        "nice thank you",
        "thanks buddy",
        "cheers",
        "alright thanks"
      ],
      "answers": [
        "Anytime. That's what I'm here for",
        "It's my pleasure to help"
      ]
    },
    {
      "intent": "greetings.bye",
      "utterances": [
        "goodbye for now",
        "bye bye take care",
        "okay see you later",
        "bye for now",
        "I must go"
      ],
      "answers": [
        "Till next time",
        "see you soon!"
      ]
    },
    {
      "intent": "greetings.hello",
      "utterances": [
        "hello",
        "hi",
        "howdy"
      ],
      "answers": [
        "Hey there!",
        "Greetings!"
      ]
    },
    {
      "intent": "user.testing",
      "utterances": [
        "test",
        "testing",
        "testing chatbot",
        "this is a test",
        "just testing you"
      ],
      "answers": [
        "I like being tested. It helps keep me sharp",
        "I hope to pass your tests. Feel free to test me often"
      ]
    },
    {
      "intent": "user.needsadvice",
      "utterances": [
        "I need advice",
        "I need some advice",
        "can you give me some advice?",
        "what should I do?"
      ],
      "answers": [
        "I probably won't be able to give you the correct answer right away",
        "I'm not sure I'll have the best answer, but I'll try"
      ]
    },
    {
      "intent": "None",
      "utterances": [
        "I need advice",
        "I need some advice",
        "can you give me some advice?",
        "what should I do?"
      ],
      "answers": [
        "Sorry, I don't understand"
      ]
    }
  ]
}


//normalize -> tokenize -> stem -> removeStopwords
//searches in pairs if input is included | pairs = dic -> array -> dic -> array { [ { [ ] } ] }
function getBotResponse(input){
  if (input.length < 3) {return "Könnten Sie bitte eine längere Eingabe formulieren?";}

  let tokAndStem = stemmer.tokenizeAndStem(input);
  let final = stopwords.removeStopwords(tokAndStem)
  console.log(final)
  for (let i = 0; i < pairs?.data.length; i++) {
    for (let j = 0; j < pairs.data[i].utterances.length; j++) {
      let arr = pairs.data[i].utterances[j].split()
      let found = arr.some(r => final.includes(r));
      //let found = _.some(arr, final)
        if (found) {
           return pairs.data[i].answers[j];
        } 
    }
  }
  return "Könnten Sie die Eingabe anders formulieren?"; 
}


const input = 'i am wondering if testing your developer is needed';
//console.log(stemmer.tokenizeAndStem(input));
console.log(getBotResponse(input))

//Deutsche Variante
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