//collapsible
var coll = document.getElementsByClassName("collapsible");

//click to open chat
for (let i = 0;i < coll.length; i++){
    coll[i].addEventListener("click", function(){
        this.classList.toggle("active");
    
        var content = this.nextElementSibling;

        if (content.style.maxHeight){
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}

//get time for first message
function getTime(){
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10){
        hours = "0" + hours
    }

    if (minutes < 10){
        minutes = "0" + minutes
    }

    let time = hours + ":" + minutes;
    return time; 
}




// Gets the first message
function firstBotMessage() {
    let firstMessage = "Wie darf ich behilflich sein?"
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

function getHardResponse(userText){
    let botResponse = getBotResponse(userText)
    let botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function getResponse(){
    let userText = $("#textInput").val();
    
    if (userText == ""){
        return
    }

    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout(() => {
        getHardResponse(userText);
    }, 1000)

}

function sendButton(){
    getResponse();
}

//Press enter to send message
$("#textInput").on("keypress", function(e) {
    if (e.key === "Enter") {
      getResponse();
    }
  });

