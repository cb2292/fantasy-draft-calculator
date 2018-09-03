// JavaScript Document

$(document).ready(function() {
	$(".ishidden").hide();
	$(".faq_link").click(function() {
			$(this).parent().next().toggle();
	});
});
