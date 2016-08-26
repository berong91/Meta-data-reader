/**
 * Created by DUY on 2016-08-21.
 */
function reloadData() {
    $.ajax({
        url: "update",
        beforeSend: function () {
            $('#record-panel').html('<div class="loading"><img src="/static/meta_reader/img/loading.gif" alt="Loading..." /></div>');
            $('#source-source').html('<div class="loading"><img src="/static/meta_reader/img/loading.gif" alt="Loading..." /></div>');
        },
        success: function (data) {
            $('#record-panel').empty();
            $('#source-panel').empty();
            handleData(data);
        },
        error: function () {
            $('#record-panel').html('<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>');
            $('#source-panel').html('<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>');
        }

    });

}

setInterval(function () {
    reloadData() // this will run after every 5 seconds
}, 10000);

function handleData(data) {
    $('#source-panel').html(data.status);

    $('#record-panel').html('<table class="table table-bordered" id="source-tbl"><thead><tr><th>ID</th><th>Source</th><th>Date</th><th>FileName</th><th>Acion</th><th>Rating</th><th>Submit type</th></tr></thead>');
    $.each(JSON.parse(data.records), function (index, element) {
        var colour;
        if (element.fields.rating == 'clean')
            colour = "active";
        else if (element.fields.rating == 'low-risk')
            colour = "info";
        else if (element.fields.rating == 'medium-risk')
            colour = "warning";
        else if (element.fields.rating == 'high-risk')
            colour = "danger";
        else if (element.fields.rating == 'malicious')
            colour = "success";

        var html = '<tr class="' + colour + '">' + '<td>' + element.pk + '</td>' + '<td>' + element.fields.source + '</td>' + '<td>' + element.fields.date + '</td>' + '<td>' + element.fields.filename + '</td>' + '<td>' + element.fields.action + '</td>' + '<td>' + element.fields.rating + '</td>' + "<td>" + element.fields.submit_type + "</td>" + '</tr>' + '</tbody></table>';
        $('#source-tbl').append(html);
    });
}