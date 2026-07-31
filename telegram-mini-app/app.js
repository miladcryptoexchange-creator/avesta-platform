// Telegram WebApp init
const tg = window.Telegram.WebApp;
tg.expand();

// State
let miningActive = false;
let timeLeft = 86400;
let boost = 0;
let spinsToday = 0;

// Mining functions
function startMining() {
    miningActive = true;
    document.getElementById('miningSection').style.display = 'block';
    updateTimer();
    setInterval(updateTimer, 1000);
    
    // Show ad on start
    showAd();
}

function updateTimer() {
    if (timeLeft > 0) {
        timeLeft--;
        const h = Math.floor(timeLeft / 3600);
        const m = Math.floor((timeLeft % 3600) / 60);
        const s = timeLeft % 60;
        document.getElementById('timer').textContent = 
            `${h.toString().padStart(2,'0')}:${m.toString().padStart(2,'0')}:${s.toString().padStart(2,'0')}`;
    }
}

function watchAd() {
    if (boost < 10) {
        showAd();
        boost += 2;
        document.getElementById('boostPercent').textContent = boost;
        tg.HapticFeedback.impactOccurred('light');
    } else {
        tg.showAlert('Daily ad limit reached!');
    }
}

function showAd() {
    // Simulate ad
    tg.showPopup({
        title: 'Watch Ad',
        message: 'Watch a short video to boost your mining rate!',
        buttons: [{id: 'watch', text: 'Watch'}, {id: 'skip', text: 'Skip'}]
    });
}

// Lucky Spin
function luckySpin() {
    if (spinsToday >= 2) {
        tg.showPopup({
            title: 'No Free Spins',
            message: 'Watch an ad for 3 extra spins!',
            buttons: [{id: 'watch_ad', text: 'Watch Ad'}, {id: 'cancel', text: 'Cancel'}]
        });
        return;
    }
    
    spinsToday++;
    const rewards = ['1 AVN', '5 AVN', '10 AVN', '50 XP', 'Badge', 'Mystery Box', '100 AVN'];
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    
    tg.HapticFeedback.notificationOccurred('success');
    tg.showAlert(`You won: ${reward}!`);
}

// Navigation
function openWallet() {
    tg.showAlert('Wallet feature coming soon!');
}

function openNFT() {
    tg.showAlert('NFT Marketplace coming soon!');
}

// Init
console.log('Avesta Mini App initialized');
