let end = false;

function updateProgressBar(percent) {
    $('#progress-bar').css('width', percent + '%');
}

//pobranie wszystkich slidów które zostały już zrobione
$(function() {
    function fetchData() {
        $.getJSON($SCRIPT_ROOT + '/all_slides', {}, function(data) {
            $("#result_text").append(data.result);
            updateProgressBar(data.percent);
            if (data.percent === 100){
                end=true;
            }
        });
    }

    fetchData();
});

//pobieranie slajdu po naciśnięciu
$(function() {
    $('a#next').bind('click', function() {
        console.log(end)
        if (!end)
        {
            $.getJSON($SCRIPT_ROOT + '/slide', {}, function(data) {
                $("#result_text").append(data.result);
                updateProgressBar(data.percent);
                if (data.percent === 100) end=true
            });
        }
        return false;
    });
});

