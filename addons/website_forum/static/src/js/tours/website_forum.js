/** @odoo-module **/

    import { _t } from "@web/core/l10n/translation";
    import wTourUtils from "@website/js/tours/tour_utils";

    wTourUtils.registerBackendAndFrontendTour("question", {
        url: '/forum/1',
    }, () => [{
        trigger: ".o_wforum_ask_btn",
        position: "left",
        content: _t("Create a new post in this forum by clicking on the button."),
        run: "click",
    }, {
        trigger: "input[name=post_name]",
        position: "top",
        content: _t("Give your post title."),
        run: "edit Test",
    }, {
        trigger: ".note-editable p",
        extra_trigger: `input[name=post_name]:not(:empty)`,
        content: _t("Put your question here."),
        position: "bottom",
        run: "editor Test",
    }, {
        trigger: ".select2-choices",
        extra_trigger: `.note-editable p:not(:contains(/^<br>$/))`,
        content: _t("Insert tags related to your question."),
        position: "top",
    }, 
    {
        trigger: "input[id=s2id_autogen2]",
        run: "editor Test",
    },
    {
        trigger: "button:contains(/^Post/)",
        extra_trigger: `input[id=s2id_autogen2]:not(:contains(Tags))`,
        content: _t("Click to post your question."),
        position: "bottom",
        run: "click",
    }, {
        isActive: ["auto"],
        extra_trigger: 'div.modal.modal_shown',
        trigger: ".modal-header button.btn-close",
        run: "click",
    },
    {
        trigger: "a:contains(\"Reply\").collapsed",
        content: _t("Click to reply."),
        position: "bottom",
        run: "click",
    },
    {
        trigger: ".note-editable p",
        content: _t("Put your answer here."),
        position: "bottom",
        run: "editor Test",
    }, {
        trigger: "button:contains(\"Post Answer\")",
        extra_trigger: `.note-editable p:not(:contains(/^<br>$/))`,
        content: _t("Click to post your answer."),
        position: "bottom",
        run: "click",
    }, {
        isActive: ["auto"],
        extra_trigger: 'div.modal.modal_shown',
        trigger: ".modal-header button.btn-close",
        run: "click",
    }, {
        trigger: ".o_wforum_validate_toggler[data-karma]:first",
        content: _t("Click here to accept this answer."),
        position: "right",
        run: "click",
    }, {
        isActive: ["auto"],
        content: "Check edit button is there",
        trigger: "a:contains('Edit your answer')",
    }]);
