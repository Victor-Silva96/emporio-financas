import {sendCollaboratorUpdateForm} from "./init_modal_collaborator.js";

async function update_collaborator(url = `${window.location.origin}/collaborator`) {
    const result = await fetch(url, {
        method: "PUT",
        body: JSON.stringify(sendCollaboratorUpdateForm),
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

    const date = await result;
    if (date.status === 200) {
        remove_loading()

    }

}

function remove_loading(text) {
    $("#result-search").disable()
}

export {update_collaborator}