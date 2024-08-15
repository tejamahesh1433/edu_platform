// static/js/create_post.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Create post page loaded");
});

// Function to apply formatting to selected text in the textarea
function applyFormatting(tag) {
    var textarea = document.getElementById('content');
    var start = textarea.selectionStart;
    var end = textarea.selectionEnd;
    var selectedText = textarea.value.substring(start, end);
    var before = textarea.value.substring(0, start);
    var after = textarea.value.substring(end);
    var newText;

    switch(tag) {
        case 'bold':
            newText = before + '<strong>' + selectedText + '</strong>' + after;
            break;
        case 'italic':
            newText = before + '<em>' + selectedText + '</em>' + after;
            break;
        case 'underline':
            newText = before + '<u>' + selectedText + '</u>' + after;
            break;
    }

    textarea.value = newText;
}

// Function to preview the post
function previewPost() {
    var title = document.getElementById('title').value;
    var category = document.getElementById('category').value;
    var content = document.getElementById('content').value;

    document.getElementById('preview-title').innerText = title;
    document.getElementById('preview-category').innerText = "Category: " + category;
    document.getElementById('preview-content').innerHTML = content;
}
