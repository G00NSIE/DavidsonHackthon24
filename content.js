
/*chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extractText") {
      extractTextAsync().then(text => {
        sendResponse({text: text});
        console.log(text);
      }).catch(error => {
        console.error("Error extracting text:", error);
        sendResponse({error: error.toString()});
      })
      // Must return true to indicate you're sending a response asynchronously
      return true;
    }
  });*/

  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extractText") {
      // Extract the text from the current page and log it
      console.log(document.body.innerText);
      console.log("text printing from content.js")
      chrome.runtime.sendMessage({action: "sendNativeMessage", data: {text: "Hello, Python!"}});
    }
  });


 

  /*function extractTextAsync() {
    return new Promise((resolve, reject) => {
      try {
        // Synchronously getting all text from the webpage
        const allText = document.body.innerText;
        resolve(allText); // Resolving the promise with the text
      } catch (error) {
        reject(error); // Rejecting the promise if there's an error
      }
    });
  }
  */