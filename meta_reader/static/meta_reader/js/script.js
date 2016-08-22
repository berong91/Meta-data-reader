/**
 * Created by DUY on 2016-08-21.
 */
function reloadData() {
    $.ajax({
        url: "update",
        beforeSend: function () {
            $('#ajax-panel').html('<div class="loading"><img src="/static/meta_reader/img/loading.gif" alt="Loading..." /></div>');
        },
        success: function (data) {
            $('#ajax-panel').empty();
            handleData(data);
        },
        error: function () {
            $('#ajax-panel').html('<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>');
        }

    });

}

setInterval(function () {
    reloadData() // this will run after every 5 seconds
}, 10000);

function handleData(data) {
    $('#ajax-panel').html('<table class="table table-bordered" id="tbl"><thead><tr><th>ID</th><th>Source</th><th>Date</th><th>FileName</th><th>Acion</th><th>Rating</th><th>Submit type</th></tr></thead>');
    $.each(JSON.parse(data), function (index, element) {
        var colour;
        if (element.fields.rating =='clean')
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
        $('#tbl').append(html);
        console.log(element.fields);
    });
}