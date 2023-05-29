export let sendCollaboratorUpdateForm

export function init_modal_collaborator() {
    $("#update").click(function (event) {
        event.preventDefault();
        $('#modal1').modal('open');
        var td = $(this).parents('tr').find('td:lt(3)');

        $("#update-button").click(function (event) {
            event.preventDefault();
            console.log(td);
        })


    });
}
