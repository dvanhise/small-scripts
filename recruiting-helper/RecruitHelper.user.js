// ==UserScript==
// @name        RecruitHelper
// @namespace   RecruitingHelperScript
// @include     *cybernations.net/allNations_display.asp*
// @version     1
// @require     http://www.cybernations.net/script/jquery.min.js
// @description Creates a list of nation names from the CN nation's list
// @grant       none
// ==/UserScript==
$( document ).ready(function() {
    $(document.body).prepend('<div id="this_location"><div>');
    $location = $('#this_location');
    $("img[title^='Ruler']").each(function () {
        $this = $(this);
        if ($this.closest('p').find('img[title^="Alliance"]').length == 0) {
            text = $this.attr('title').replace('Ruler: ', '');
            $location.append(text + "<br>");
        }
    });
});