import {sendServiceForm} from "./init_service.js";

async function insert_service_collaborator(url = `${window.location.origin}/services_collaborator`) {
    const result = await fetch(url, {
        method: "POST",
        body: JSON.stringify(sendServiceForm),
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

    const date = await result;
    if (date.status === 201) {
        alarm_ok("Serviço enviado para o colaborador")
    }

}

function alarm_ok(text) {
    $("#result-search").html(`<div class="alert card green lighten-4 green-text text-darken-4">
		<div class="card-content">
			<p><i class="material-icons">check_circle</i><span>${text}</span></p>
		</div>
	</div>`).fadeIn("slow").fadeOut(2000, function () {
        $("#send").removeClass('disabled')
    })
}

export {insert_service_collaborator}