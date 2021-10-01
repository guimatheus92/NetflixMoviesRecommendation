$(document).ready(function() {
    $('#example').DataTable( {
        "columnDefs": [
            {
                "targets": [ 0 ],
                "visible": true,
                "searchable": false
            },
            {
                "targets": [ 1 ],
                "visible": true
            },
            {
                "targets": [ 2 ],
                "visible": true
            },
            {
                "targets": [ 3 ],
                "visible": true,
                "searchable": false,
                "ordering": false
            }
        ]
    } );
} );