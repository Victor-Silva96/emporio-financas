import {sendDownloadFaturamentoForm} from "./init_faturamento_pdf.js";

async function download_faturamento(url = `${window.location.origin}/faturamento_pdf/download`) {
    fetch(url, {
        method: "POST",
        body: JSON.stringify(sendDownloadFaturamentoForm),
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })

    }).then((res) => {
        return res.blob();
    })
        .then((data) => {
            const a = document.createElement("a");
            a.href = window.URL.createObjectURL(data);
            a.download = $("div#collaborator input").val()
            a.click();
            $("#result-search").empty()
            $("#download").removeClass('disabled')
            reset_fields()
        });


}


function reset_fields() {
    $("div#collaborator .select-dropdown.dropdown-trigger").val($("select#collaborator option:first").text())
    $("input#start").val('')
    $("input#end").val('')
}

export {download_faturamento}