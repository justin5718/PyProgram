var recorder;
        var audio = document.querySelector('audio');
        function startRecording() {
            HZRecorder.get(function (rec) {
                recorder = rec;
                recorder.start();
            });
        }
        function stopRecording() {
            recorder.stop();
        }
        function playRecording() {
            recorder.play(audio);
        }
        function uploadAudio() {
            recorder.upload();
        }
        function fucktest() {
            var languages = $("input[name='language']:checked").val();
            alert(languages);
        }