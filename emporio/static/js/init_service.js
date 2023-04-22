import {insert_service_collaborator} from "./insert_service_collaborator.js";
import {set_loader} from "./loader.js";

export let sendServiceForm

export function init_service() {
    $("#send").click(function () {
        clearValidations()
        sendServiceForm = {};
        sendServiceForm.collaborator = $("select#collaborator").val();
        sendServiceForm.services = $("select#services").formSelect('getSelectedValues');
        sendServiceForm.client = $("input#client").val();
        sendServiceForm.serviceData = $("input#service-data").val();
        /*    sendServiceForm.sample = $("#sample").val();*/
        if (validateFields()) {
            $("#send").addClass('disabled')
            set_loader();
            setTimeout(function () {
                insert_service_collaborator()
            }, 1500);
        }
    });
}

function validateFields() {
    let validate = true
    let templateError = `<span class="helper-text" data-error="{}"></span>`
    if (!sendServiceForm.client) {
        $("div#client").append(templateError.replace("{}", "Campo cliente obrigátorio"))
        $("div #client").addClass('invalid')
        validate = false
    }
    if (!sendServiceForm.services.length) {
        $("div#services .select-wrapper input")
            .after(templateError.replace("{}", "Campo de serviços obrigátorio"))
            .addClass('invalid')
        validate = false
    }
    return validate;
}

function clearValidations() {
    $("span.helper-text").remove()
    $("div #client").removeClass('invalid')
    $("div#services .select-wrapper input").removeClass('invalid')

}