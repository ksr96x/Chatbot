//var natural = require("natural");
const { NlpManager } = require('node-nlp');
const {SentimentAnalyzer} = require('node-nlp');

const sentiment = new SentimentAnalyzer({language:'de'});
//var tokenizer = new natural.WordTokenizer();
const stemmed = new NlpManager({language: 'de'});

sentiment
    .getSentiment('Ich mag Katzen')
    .then(result => console.log(result));

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

//searches in pairs if input is included | pairs = dic -> array -> dic -> array { [ { [ ] } ] }
function getBotResponse(input){
  var tokenized = tokenizer.tokenize(input)
  for (let i = 0; i < pairs.data.length; i++) {
    for (let j = 0; j < pairs.data[i].utterances.length; j++) {
        if (pairs.data[i].utterances[j].includes(tokenized)) {
           return pairs.data[i].answers[j];
        } 
    }
  }
  return "Könnten Sie die Eingabe anders formulieren?"; 
}