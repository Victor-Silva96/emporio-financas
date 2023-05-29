import {set_loader} from "./loader.js";
import {update_collaborator} from "./update_collaborator.js";
export let sendCollaboratorUpdateForm

export function init_modal_collaborator() {
   $('.btn-floating.pink.accent-1').click(function () {
        $('#modal1').modal('open');
        let td = $(this).parents('tr').find('td:lt(3)');
        $('#name').val(td[0].textContent);
        $("#update-button").click(function (event) {
            event.stopPropagation();
            sendCollaboratorUpdateForm = {}
            sendCollaboratorUpdateForm.collaborator_id = td[0].getAttribute('value')
            sendCollaboratorUpdateForm.collaborator_name = $("#name").val()
            set_loader();
            setTimeout( function () {
                update_collaborator()
            }, 1500)
            td[0].textContent = $("#name").val()
        })
    });
}
