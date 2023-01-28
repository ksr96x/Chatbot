import * as nltk from 'nltk';
import { Chat, reflections } from 'nltk/chat/util';
import * as time from 'time';
var bot_name, chatbot;

class Chatbot {
  constructor() {
    this.pairs = [["Ich habe eine Frage zu (.*)", 
    ["Was möchten Sie speziell zu %1 wissen?"]], 

    ["Wie kann ich mich bewerben?|bewerben|(.*) bewerben|bewerben (.*)", 
    ["Wenn Sie sich bewerben wollen, können Sie ganz einfach eine Email mit Lebenslauf an xxx senden"]],

    ["(.*) Telefonnummer", ["Unsere Telefonnummer ist 123456789"]], ["(.*)", 
    ["Ich habe Ihre Eingabe leider nicht verstanden. Könnten Sie das bitte anders formulieren?"]]];
  }

}

chatbot = new Chat(new Chatbot().pairs, reflections);
bot_name = "Sam";

function main() {
  var answer, question;
  console.log(`${bot_name}: Willkommen bei Firma xyz`);
  time.sleep(2);
  console.log(`${bot_name}: Um Hilfe zu bekommen, drücken Sie Start`);
  console.log(`${bot_name}: Wie darf ich Ihnen helfen?`);

  while (true) {
    question = input("Sie: ").toString().lower();

    if (question === "ende") {
      console.log(`${bot_name}: Zögern Sie nicht, mich wieder zu kontaktieren!`);
      break;
    }

    answer = chatbot.respond(question);
    console.log(`${bot_name}: ${answer}`);
    time.sleep(2);
    console.log(`${bot_name}: Kann ich Ihnen sonst noch etwas beantworten?`);
  }
}

main(); 




