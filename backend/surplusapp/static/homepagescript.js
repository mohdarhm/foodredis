const revealButton = document.getElementById('revealButton');
const cardContainer = document.getElementById('cardContainer');
const cardContainer2 = document.getElementById('cardContainer2');

revealButton.addEventListener('click', () => {
    cardContainer.style.display = 'grid';
    revealButton.style.display = 'none';
    console.log("script loaded");
});

// Attach the event listener to a parent element that is not dynamically created
cardContainer.addEventListener('click', (event) => {
    const regButton = document.getElementById('regbutton');
    
    // Check if the clicked element is the regButton
    if (event.target === regButton) {
        console.log("reg button");
        // Perform your actions here
        

        cardContainer2.style.display ='grid';
        // cardContainer.style.display ='none';
    }
});
