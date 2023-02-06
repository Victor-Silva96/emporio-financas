import {download_faturamento} from "./download_faturamento_pdf.js";
import {set_loader} from "./loader.js";

export let sendDownloadFaturamentoForm

export function init_search_characteristics() {
    $("#download").click(function () {
        clearValidations()
        sendDownloadFaturamentoForm = {};
        sendDownloadFaturamentoForm.collaborator = $("select#collaborator").val();
        sendDownloadFaturamentoForm.start = $("input#start").val();
        sendDownloadFaturamentoForm.end = $("input#end").val();
        if (validateFields()) {
            $("#download").addClass('disabled')
            set_loader();
            setTimeout(function () {
                download_faturamento()
            }, 1500);
        }
    });
}

function validateFields() {
    let validate = true
    let templateError = `<span class="helper-text" data-error="{}"></span>`
    if (!sendDownloadFaturamentoForm.start) {
        $("div#start").append(templateError.replace("{}", "Campo data inicio obrigátorio"))
        $("div #start").addClass('invalid')
        validate = false
    }
    if (!sendDownloadFaturamentoForm.end) {
        $("div#end").append(templateError.replace("{}", "Campo data fim obrigátorio"))
        $("div #end").addClass('invalid')
        validate = false
    }
    return validate;
}

function clearValidations() {
    $("span.helper-text").remove()
    $("div #start").removeClass('invalid')
    $("div #end").removeClass('invalid')

}