chrome.webRequest.onBeforeRequest.addListener(
    function(result){
        console.log(result.url);
        return{cancel: true };
    },
    {urls: blocked_domains},
    ["blocking"]

)
