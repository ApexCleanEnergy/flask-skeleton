function checkUser(params) {

    function autoSubmitName(uName) {
        if (uName === "silas.frantz") {
            console.log("Hey Silas... enjoy the admin rights!");
        }
        else {
            location = '?user=' + uName.split('.').map(w => w[0].toUpperCase() + w.substr(1)).join(' ') + params;
        }
    }
    require(["esri/identity/IdentityManager"],
        function (esriID) {
            var testURL = "https://gis.apexcleanenergy.com/portal/sharing/rest";
            esriID.checkSignInStatus(testURL)
                .then(
                    function (checkResult) {
                        autoSubmitName(checkResult.userId)
                    },
                    function (error) {
                        console.warn(error);
                    })
        }
    );
};