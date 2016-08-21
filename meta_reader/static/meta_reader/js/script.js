/**
 * Created by DUY on 2016-08-21.
 */
function reloadData() {
    $('#links').load('/update', function () {
        $(this).unwrap();
    });
}

setInterval(function () {
    reloadData() // this will run after every 5 seconds
}, 5000);
