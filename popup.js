document.getElementById('extractText').addEventListener('click', () => {    
    // Query the current active tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        // Send a message to the content script of the active tab
        chrome.tabs.sendMessage(tabs[0].id, {action: "extractText"});
    });
});
