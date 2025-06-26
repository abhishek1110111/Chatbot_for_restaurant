document.addEventListener('DOMContentLoaded', function() {
    const chatIcon = document.getElementById('chatIcon');
    const chatbotIframe = document.getElementById('chatbotIframe');
    const initialChatButton = document.getElementById('initialChatButton'); // New reference
    const hideChatbotButton = document.getElementById('hideChatbotButton');

    // Select the actual Font Awesome icons within the chatIcon
    const chatBubbleIcon = chatIcon.querySelector('.fa-comment-dots');
    const downArrowIcon = chatIcon.querySelector('.fa-arrow-down');

    // Initial state: hide chatbot, hide "Hide Chatbot" button, show "Chat with Abhi" button, show chat bubble icon
    chatbotIframe.classList.remove('active');
    if (hideChatbotButton) hideChatbotButton.style.display = 'none';
    if (initialChatButton) initialChatButton.style.display = 'block'; // Ensure initial button is visible
    if (chatBubbleIcon) chatBubbleIcon.style.display = 'block';
    if (downArrowIcon) downArrowIcon.style.display = 'none';

    function toggleChatbot() {
        const isActive = chatbotIframe.classList.toggle('active');

        if (isActive) {
            // Chatbot is open
            if (initialChatButton) initialChatButton.style.display = 'none'; // Hide initial button
            if (hideChatbotButton) hideChatbotButton.style.display = 'block'; // Show hide button
            
            if (chatBubbleIcon) chatBubbleIcon.style.display = 'none'; // Hide chat bubble icon
            if (downArrowIcon) downArrowIcon.style.display = 'block'; // Show down arrow
        } else {
            // Chatbot is closed
            if (initialChatButton) initialChatButton.style.display = 'block'; // Show initial button
            if (hideChatbotButton) hideChatbotButton.style.display = 'none'; // Hide hide button

            if (chatBubbleIcon) chatBubbleIcon.style.display = 'block'; // Show chat bubble icon
            if (downArrowIcon) downArrowIcon.style.display = 'none'; // Hide down arrow
        }
    }

    // Event listeners
    if (chatIcon) chatIcon.addEventListener('click', toggleChatbot);
    if (initialChatButton) initialChatButton.addEventListener('click', toggleChatbot);
    if (hideChatbotButton) hideChatbotButton.addEventListener('click', toggleChatbot);
});