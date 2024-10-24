<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>  سعرك بيدك</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

    <link rel="manifest" href="manifest.json">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <link rel="apple-touch-icon"
        href="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737">
    <meta name="apple-mobile-web-app-status-bar" content="#db4938">
    <meta name="theme-color" content="#db4938">
    <link rel="stylesheet" href="css/style.css">
    <script src="https://unpkg.com/react/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/babel-standalone/babel.min.js"></script>
 <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-storage.js"></script>
 
 <script src="firebase-config.js"></script>
    <script src="script.js"></script>

    
<style>
    :root {
    --primary-color: #2E1A47; /* Dark purple matching the nebula */
    --secondary-color: #8B4896; /* Soft purple accent from the nebula */
    --accent-color: #FFD700; /* Golden yellow for contrast with the dark background */
    --text-color: #FFFFFF; /* White text to stand out against dark colors */
    --background-color: #0A0014; /* Very dark purple, almost black */
    --card-background: #2E1A47; /* Darker shade of purple for card backgrounds */
    --header-background: #27053C; /* Deep space purple for headers */
    --header-text: #FFFFFF; /* White for clear readability */
    --shadow-color: rgba(255, 255, 255, 0.2); /* Soft white shadow for depth */
    --button-hover-color: #DDA0DD; /* Light lavender for hover effect */
}



body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: var(--background-color);
    color: var(--text-color);
    transition: background-color 0.3s ease;
    background-image: url('https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2Fpngwing.com%20(1).png?alt=media&token=f4b65dff-469f-4466-9e2b-9fb5f1e54119');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    padding-bottom: 90px;
}

.header {
    background-color: var(--header-background);
    color: var(--header-text);
    padding-top: 1px;   /* التحكم في المسافة الداخلية من الأعلى */
    padding-bottom: -100px; /* التحكم في المسافة الداخلية من الأسفل */
    margin-top: -20px;    /* التحكم في المسافة من أعلى الصفحة أو العناصر الأخرى */
    margin-bottom: 20px; /* التحكم في المسافة من أسفل شريط العنوان */
    position: fixed;     /* لإبقاء شريط العنوان ثابتًا في أعلى الصفحة */
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;       /* للتأكد من بقاء العنوان فوق جميع العناصر */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* إضافة ظل */
}


.carousel {
    width: 100%;
    height: 200px; /* ارتفاع شريط الإعلان */
    margin-top: 158px; /* التحكم في المسافة من الأعلى */
    margin-bottom: 10px; /* التحكم في المسافة من الأسفل */
    padding-top: 30px; /* إضافة فراغ داخلي من الأعلى */
    padding-bottom: 10px; /* إضافة فراغ داخلي من الأسفل */
    position: relative;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

 /* خانة التصنيف */
 #categorySelect {
    margin-top: 0px;
    width: 100%;
    padding: 1px;
    font-size: 0.5rem;
    border: 0px solid #ccc;
    border-radius: 15px;
}
.header-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.header h1 {
    margin: 0 0 0.8rem;
    font-size: 1.3rem;
    text-align: center;
}

.header-controls {
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: center;
}

.search-container {
    position: relative;
    width: 100%;
    max-width: 500px;
    margin-bottom: 0.5rem;
}

.search-icon {
    position: absolute;
    left: 10px;
    top: 70%;
    transform: translateY(-50%);
    color: #FFFFFF;
    cursor: pointer;
}

#searchInput {
padding: 10px 30px; /* تعديل القيم لزيادة أو تقليل المسافة الداخلية */
    margin-top: 10px; /* المسافة العلوية */
    margin-bottom: 1px; /* المسافة السفلية */
    border-radius: 20px; /* تعديل شكل الحواف */
    width: 100%;
    padding: 0.5rem 2rem;
    border-radius: 20px;
    border: none;
    outline: none;
    background-color: rgba(255, 255, 255, 0.1);
    color: var(--header-text);
    transition: background-color 0.3s ease;
}

#searchInput::placeholder {
    color: rgba(255, 255, 255, 0.7);
}

#searchInput:focus {
    background-color: rgba(255, 255, 255, 0.2);
}

.header-button {
    background: none;
    border: none;
    color: var(--header-text);
    font-size: 1.2rem;
    cursor: pointer;
    margin-left: 1rem;
    transition: color 0.3s ease;
}

.header-button:hover {
    color: var(--accent-color);
}

.sidebar {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1001;
    top: 0;
    right: 0;
    background-color: var(--header-background);
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
    box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
}

.sidebar a {
    padding: 15px 25px;
    text-decoration: none;
    font-size: 18px;
    color: var(--header-text);
    display: block;
    transition: 0.3s;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.sidebar .closebtn {
    position: absolute;
    top: 0.5rem;
    left: 25px;
    font-size: 36px;
    margin-right: 50px;
}

.sidebar-icon {
    margin-right: 5px;
    width: 10px;
    text-align: center;
}

.products {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(p10px, 1fr));
    gap: 1rem;
    padding: 1rem;
    margin-top: 350px;
    margin-bottom: 1rem;
}

.product-card {
    background-color: var(--card-background);
    border-radius: 0.8rem;
    box-shadow: 0 4px 8px var(--shadow-color);
    overflow: hidden;
    transition: transform 0.3s, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px var(--shadow-color);
}

.product-images {
    position: relative;
    height: 0;
    padding-bottom: 150%;
    overflow: hidden;
}

.product-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.product-image:not(:first-child) {
    opacity: 0;
}

.product-card:hover .product-image {
    transform: scale(1.05);
}

.image-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(255, 255, 255, 0.7);
    color: var(--text-color);
    border: none;
    font-size: 1.2rem;
    padding: 0.5rem;
    cursor: pointer;
    transition: background-color 0.3s, opacity 0.3s ease;
    opacity: 0;
}

.product-card:hover .image-nav {
    opacity: 1;
}

.image-nav:hover {
    background-color: rgba(255, 255, 255, 0.9);
}

.image-nav.prev {
    left: 0.5rem;
}

.image-nav.next {
    right: 0.5rem;
}

.product-info {
    padding: 0.8rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.product-info h3 {
    margin: 0 0 0.5rem;
    color: var(--primary-color);
    font-size: 1rem;
    line-height: 1.3;
}

.price-action {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
}

.price {
    font-weight: bold;
    color: var(--accent-color);
    font-size: 1rem;
}

.action-buttons {
    display: flex;
    gap: 0.5rem;
}

.action-button {
    background-color: transparent;
    border: none;
    color: var(--text-color);
    cursor: pointer;
    font-size: 1rem;
    transition: color 0.3s ease;
    display: flex;
    align-items: center;
}

.action-button:hover {
    color: var(--primary-color);
}

.action-count {
    margin-right: 0.25rem;
    font-size: 0.8rem;
    background-color: var(--primary-color);
    color: white;
    border-radius: 50%;
    padding: 0.1rem 0.3rem;
}

.buy-button {
    background-color: var(--secondary-color);
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.8rem;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
    width: 100%;
    margin-top: 0.75rem;
    font-size: 0.9rem;
    font-weight: bold;
    text-transform: uppercase;
}

.buy-button:hover {
    background-color: #2ecc71;
    transform: translateY(-2px);
}

.popup {
    display: none;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background-color: var(--card-background);
    padding: 1.5rem;
    border-radius: 1rem;
    box-shadow: 0 6px 20px var(--shadow-color);
    z-index: 1002;
    text-align: center;
    max-width: 90%;
    width: 300px;
}

.popup h3 {
    margin-bottom: 1rem;
    color: var(--primary-color);
    font-size: 1.2rem;
    font-weight: bold;
}

.popup button {
    padding: 0.5rem 1rem;
    margin: 0.5rem;
    background-color: var(--secondary-color);
    color: white;
    border: none;
    border-radius: 0.8rem;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
    font-size: 0.9rem;
    font-weight: bold;
}

.popup button:hover {
    background-color: #2ecc71;
    transform: translateY(-2px);
}

.timer {
    font-size: 1.8rem;
    color: var(--accent-color);
    margin-bottom: 1rem;
    font-weight: bold;
}

.popup .closebtn {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    background-color: transparent;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--text-color);
}

.popup .closebtn:hover {
    color: var(--accent-color);
}

.price-display {
    font-size: 1.2rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-weight: bold;
}

.add-product-btn {

    position: fixed;
    bottom: 5rem;
    left: 1rem;
    background-color: var(--primary-color);
    color: white;
    padding: 0.75rem;
    border-radius: 50%;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 4px 12px var(--shadow-color);
    z-index: 1003;
}

.add-product-btn:hover {
    background-color: var(--secondary-color);
    transform: scale(1.1);
}

.add-product-form {
    display: none;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background-color: var(--card-background);
    padding: 1.5rem;
    border-radius: 1rem;
    box-shadow: 0 6px 20px var(--shadow-color);
    z-index: 1002;
    text-align: right;
    max-width: 90%;
    width: 300px;
}

.add-product-form h3 {
    margin-bottom: 1rem;
    color: var(--primary-color);
    font-size: 1.2rem;
    font-weight: bold;
}

.add-product-form input,
.add-product-form select {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 0.5rem;
    font-size: 0.9rem;
}

.add-product-form button {
    background-color: var(--secondary-color);
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.8rem;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
    font-size: 0.9rem;
    font-weight: bold;
}

.add-product-form button:hover {
    background-color: #2ecc71;
    transform: translateY(-2px);
}

.dark-mode {
   --primary-color: #2C3E50; /* لون أساسي: أزرق داكن */
    --secondary-color: #871515; /* لون ثانوي: أخضر داكن */
    --accent-color: #F39C12; /* لون تمييز: برتقالي */
    --text-color: #000000; /* لون النص: أزرق داكن */
    --background-color: #000000; /* لون الخلفية: رمادي فاتح */
    --card-background: #000000; /* لون خلفية البطاقة: أبيض */
    --header-background: #000000; /* لون خلفية العنوان: أزرق رمادي */
    --header-text: #F39C12; /* لون نص العنوان: رمادي فاتح */
    --shadow-color: rgba(0, 0, 0, 0.1); /* لون الظل: أسود شفاف */
    --button-hover-color: #E67E22; /* لون الأزرار عند التمرير: برتقالي داكن */
}


.cart-button {
    position: fixed;
    bottom: 5rem;
    right: 1rem;
    background-color: var(--primary-color);
    color: white;
    padding: 0.75rem;
    border-radius: 50%;
    font-size: 1.5rem;
    border: none;
    cursor: pointer;
    z-index: 1002;
    box-shadow: 0 4px 12px var(--shadow-color);
    transition: 0.3s ease;
}

.cart-button:hover {
    background-color: var(--secondary-color);
    transform: translateY(-3px);
}

.cart-count {
    position: absolute;
    top: -0.25rem;
    right: -0.25rem;
    background-color: var(--accent-color);
    color: white;
    border-radius: 50%;
    padding: 0.15rem 0.3rem;
    font-size: 0.75rem;
}

.bottom-navbar {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: var(--header-background);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 0.5rem 0;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1001;
}

.nav-item {
    text-align: center;
    color: #fff;
    text-decoration: none;
    flex: 1;
    padding: 0.3rem;
    transition: background-color 0.3s ease;
}

.nav-item i {
    font-size: 1.2rem;
}

.nav-item span {
    display: block;
    font-size: 0.7rem;
    margin-top: 0.1rem;
}

.nav-item:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.nav-item:active {
    background-color: rgba(255, 255, 255, 0.2);
}

.floating-info {
    position: fixed;
    top: 10px;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
    z-index: 1000;
    gap: 50px;
}


.digital-clock, .subscriber-count {
    background-color: var(--header-background);
    color: white;
    padding: 20px 10px;
    border-radius: 15px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    font-size: 0.20rem;
    font-weight: bold;
}

.flip-card {
    background-color: var(--header-background);
    color: #fff;
    display: inline-block;
    padding: 3px;
    margin: 0 2px;
    border-radius: 5px;
    box-shadow: 0 1px 5px rgba(0,0,0,0.3);
    perspective: 200px;
    transition: transform 0.3s;
}

.flip-card.flip {
    transform: rotateX(360deg);
}

@media screen and (max-width: 768px) {
    body {
        font-size: 12px;
    }

    .header {
        padding: 0.5rem;
    }

    .header h1 {
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }

    .header-controls {
        flex-wrap: wrap;
    }

    .search-container {
        margin-bottom: 0.5rem;
    }

    .products {
        grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
        gap: 0.8rem;
        padding: 0.8rem;
        margin-top: 0px;
    }

    .product-card {
        border-radius: 0.7rem;
    }

    .product-info {
        padding: 0.7rem;
    }

    .product-info h3 {
        font-size: 0.9rem;
    }

    .price {
        font-size: 0.9rem;
    }

    .action-button {
        font-size: 0.9rem;
    }

    .buy-button {
        padding: 0.4rem 0.8rem;
        font-size: 0.8rem;
    }

    .popup {
        padding: 1rem;
        width: 280px;
    }

    .popup h3 {
        font-size: 1.1rem;
    }

    .popup button {
        padding: 0.4rem 0.8rem;
        font-size: 0.8rem;
    }

    .timer {
        font-size: 1.5rem;
    }

    .price-display {
        font-size: 1.1rem;
    }

    .add-product-btn, .cart-button {
        bottom: 4.5rem;
        padding: 0.6rem;
        font-size: 1.3rem;
    }

    .add-product-form {
        padding: 1rem;
        width: 280px;
    }

    .add-product-form h3 {
        font-size: 1.1rem;
    }

    .add-product-form input,
    .add-product-form select {
        padding: 0.4rem;
        font-size: 0.8rem;
    }

    .add-product-form button {
        padding: 0.4rem 0.8rem;
        font-size: 0.8rem;
    }

    .nav-item i {
        font-size: 1rem;
    }

    .nav-item span {
        font-size: 0.6rem;
    }

    .floating-info {
        top: 5px;
        padding: 0 10px;
        gap: 15px;
    }

    .digital-clock, .subscriber-count {
        font-size: 0.8rem;
        padding: 3px 8px;
    }
}

@media screen and (max-width: 880px) {
    .products {
        grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
        gap: 0.6rem;
        padding: 0.6rem;
        margin-top150px;
    }

    .product-card {
        border-radius: 0.6rem;
    }

    .product-info {
        padding: 0.6rem;
    }

    .product-info h3 {
        font-size: 0.8rem;
    }

    .price {
        font-size: 0.8rem;
    }

    .action-button {
        font-size: 0.8rem;
    }

    .buy-button {
        padding: 0.3rem 0.6rem;
        font-size: 0.7rem;
    }

    .add-product-btn, .cart-button {
        bottom: 4rem;
        padding: 0.5rem;
        font-size: 1.2rem;
    }

    .nav-item {
        padding: 0.2rem;
    }

    .nav-item i {
        font-size: 0.9rem;
    }

    .nav-item span {
        font-size: 0.5rem;
    }

    .floating-info {
        flex-direction: column;
        align-items: flex-end;
        top: 3px;
        right: 5px;
        left: auto;
        gap: 5px;
    }

    .digital-clock, .subscriber-count {
        font-size: 0.7rem;
        padding: 2px 6px;
    }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideIn {
    from {
        transform: translateY(20px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.product-card {
    animation: fadeIn 0.3s ease-in-out;
}

.popup,
.add-product-form {
    animation: slideIn 0.3s ease-out;
}

.buy-button,
.action-button,
.header-button {
    transition: all 0.2s ease-in-out;
}

.buy-button:active,
.action-button:active,
.header-button:active {
    transform: scale(0.95);
}

button:focus,
input:focus,
select:focus {
    outline: 2px solid var(--accent-color);
    outline-offset: 2px;
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--background-color);
}

::-webkit-scrollbar-thumb {
    background: var(--primary-color);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--secondary-color);
}

     /* إعدادات الزر المنبثق */
.popup-button {
    position: fixed;
    bottom: 3.5rem;
    right: 0.5rem;
    background-color: #2C3E50; /* اللون الأساسي */
    color: #FFC107;
    padding: 1rem;
    border-radius: 50%;
    font-size: 1.5rem;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease, transform 0.3s ease;
    z-index: 1000;
}

.popup-button:hover {
    background-color: #2C3E50; /* اللون عند التمرير */
    transform: scale(1.1); /* تكبير الزر قليلاً عند التمرير */
}

.popup-button:active {
    transform: scale(1.65); /* تصغير الزر قليلاً عند الضغط */
}

/* العداد داخل الزر */
.cart-count {
    position: absolute;
    top: -0.25rem;
    right: -0.25rem;
    background-color: #cd2020; /* لون العداد */
    color: white;
    border-radius: 100%;
    padding: 0.2rem 0.4rem;
    font-size: 0.75rem;
    font-weight: bold;
    box-shadow: 0 12px 114px rgba(0, 0, 0, 0.2);
}


    .custom-select {
        width: 100%;
        padding: 12px;
        border: 2px solid #2C3E50; /* لون الحدود */
        border-radius: 10px; /* حواف مستديرة */
        font-size: 1.1rem; /* حجم النص */
        background-color: #fff; /* لون الخلفية */
        color: #2C3E50; /* لون النص */
        appearance: none; /* إخفاء الأسهم الافتراضية للقائمة المنسدلة */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* إضافة ظل */
        transition: border 0.3s ease, box-shadow 0.3s ease; /* تأثير الانتقال */
        position: relative;
        cursor: pointer;
    }

    .custom-select:hover, 
    .custom-select:focus {
        border-color: #27AE60; /* تغيير لون الحدود عند التمرير أو التركيز */
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2); /* تكثيف الظل عند التمرير أو التركيز */
    }

    .custom-select::after {
        content: '\25BC'; /* السهم الافتراضي للقائمة المنسدلة */
        position: absolute;
        top: 50%;
        right: 12px;
        transform: translateY(-50%);
        color: #2C3E50; /* لون السهم */
        pointer-events: none; /* منع التفاعل مع السهم */
    }

    .custom-select option {
        padding: 10px;
        background-color: #871515; /* خلفية العناصر */
        color: #871515; /* لون النص داخل العناصر */
    }


    .popup-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }
    
    .popup-content {
        background-color: #000000;
        padding: 20px;
        border-radius: 10px;
        width: 300px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .close-popup {
        margin-top: 10px;
        background-color: #f44336;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    
  
    
     .loginWithEmail {
        margin-top: 10px;
        background-color: #f44336;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    
    .popup-content input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    
    .social-login button {
        margin: 5px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    input[type="email"], input[type="password"] {
        width: 100%;
        padding: 12px;
        margin: 10px 0;
        border-radius: 5px;
        border: 1px solid #ccc;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        font-size: 1rem;
    }
    


    
   .popup1-button {
    position: fixed;
    bottom: 4rem;
    right: 18rem; /* Adjust this value to place buttons next to each other */
    background-color: #2C3E50;
    color: #FFC107;
    padding: 1rem;
    border-radius: 50%;
    font-size: 1.5rem;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease, transform 0.3s ease;
    z-index: 1000;
}

.message-count {
    position: absolute;
    top: -5px;
    right: -5px;
    background-color: #FF5733; /* يمكنك تغيير اللون كما تريد */
    color: white;
    border-radius: 50%;
    padding: 0.3rem 0.6rem;
    font-size: 0.9rem;
    font-weight: bold;
    z-index: 1001;
}

    /* الإعلان */

.carousel img {
    width: 100%;
    height: 100%;
    object-fit: cover; /* لضمان أن الصورة تغطي العنصر بشكل كامل بدون تمدد */
    position: absolute;
    top: 0;
    left: 200%;
    transition: left 1s ease-in-out; /* حركة الانزلاق بين الصور */
}

.carousel img.active {
    left: 0; /* تجعل الصورة الحالية مرئية */
}
.subscriber-count {
    position: fixed; /* لجعل الزر ثابتًا في مكانه حتى عند التمرير */
    top: 0; /* المسافة من الأعلى */
    left: 0; /* المسافة من اليسار */
    margin: 10px; /* إضافة مسافة خارجية اختيارية */
    padding: 0px; /* المسافة الداخلية حول المحتوى */
    background-color: #2E1A47; /* يمكنك تعديل لون الخلفية إذا أردت */
    color: white; /* لون النص */
    z-index: 1000; /* للتأكد من أن العنصر يبقى فوق جميع العناصر الأخرى */
    border-radius: 10px; /* حواف مستديرة للعنصر */
}
#priceInHand {
    position: relative; /* يسمح بالتحكم في موقع النص */
    top: 20; /* التحكم بالمسافة من الأعلى */
    left: 0; /* التحكم بالمسافة من اليسار */
    margin-top: 29px; /* المسافة الخارجية من الأعلى */
    margin-bottom: 0px; /* المسافة الخارجية من الأسفل */
    margin-left: 20px; /* المسافة الخارجية من اليسار */
    margin-right: 20px; /* المسافة الخارجية من اليمين */
    font-size: 1.5rem; /* حجم النص */
    color: white; /* لون النص */
}

/* المتغيرات للتحكم الكامل */
:root {
  --button-bg-color: #2E1A47;      /* لون الزر */
  --button-hover-color: #2C3E50;   /* لون الزر عند التمرير */
  --button-size: 3rem;             /* حجم الزر */
  --button-padding: 0.5rem;        /* المسافة الداخلية */
  --button-radius: 50%;            /* شكل الزر دائري */
  --button-shadow: 0 8px 15px rgba(0, 0, 0, 0.2); /* ظل الزر */
  --button-margin-top: 2rem;       /* المسافة من الأعلى */
  --button-margin-bottom: 4rem;    /* المسافة من الأسفل */
  --button-margin-right: 0.8rem;     /* المسافة من اليمين */
  --button-margin-left: 0rem;      /* المسافة من اليسار */
}

/* تنسيق الزر المنبثق الرئيسي */
.popup-toggle {
  position: fixed;
  bottom: var(--button-margin-bottom);
  right: var(--button-margin-right);
  background-color: var(--button-bg-color); /* استخدام لون مخصص */
  color: white;
  width: var(--button-size); /* استخدام حجم مخصص */
  height: var(--button-size);
  padding: var(--button-padding); /* المسافة الداخلية */
  border: none;
  border-radius: var(--button-radius); /* جعل الزر دائري */
  font-size: 1rem;
  cursor: pointer;
  box-shadow: var(--button-shadow); /* تطبيق ظل الزر */
  transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

/* عند التمرير على الزر */
.popup-toggle:hover {
  background-color: var(--button-hover-color); /* تغيير لون الزر عند التمرير */
  transform: scale(1.1); /* تكبير الزر عند التمرير */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3), 0 -4px 8px rgba(0, 0, 0, 0.1); /* تعديل الظل */
}

/* الشريط المنبثق */
.popup-menu {
  display: none;
  position: fixed;
  bottom: calc(var(--button-margin-bottom) + 4rem); /* وضع القائمة المنبثقة بالنسبة للزر */
  right: var(--button-margin-right);
  background-color: rgba(255, 255, 255, 0.5); /* خلفية شفافة */
  border-radius: 10px;
  padding: 0.5rem;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 10px;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}

/* الأزرار داخل القائمة كأيقونات فقط */
.menu-item {
  background: none;
  border: none;
  padding: 0;
  color: #2C3E50;
  font-size: 2rem;
  cursor: pointer;
  transition: transform 0.3s ease;
}

/* عند التمرير على الأيقونات */
.menu-item:hover {
  transform: scale(1.2);
  color: #3498db;
}

/* تنسيق عداد الرسائل والسلة */
.cart-count, .message-count {
  position: absolute;
  top: -0.5rem;
  right: -0.5rem;
  background-color: #e74c3c;
  color: white;
  border-radius: 50%;
  padding: 0.2rem 0.5rem;
  font-size: 0.75rem;
}

.popup {
    background-color: #f5f5f5; /* لون خلفية خفيف */
    border-radius: 10px; /* زوايا دائرية للنافذة */
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2); /* ظل لخلق عمق */
    padding: 20px; /* مسافة داخلية لتنسيق المحتوى */
    max-width: 500px; /* تحديد العرض الأقصى */
    margin: 0 auto; /* جعل النافذة في المنتصف */
}

.popup h2 {
    color: #333; /* لون نص العنوان */
    font-size: 24px; /* حجم العنوان */
    text-align: center; /* توسيط العنوان */
    margin-bottom: 20px;
}

.popup p {
    color: #555; /* لون النص */
    font-size: 16px; /* حجم النص */
    line-height: 1.5; /* تباعد بين الأسطر */
}

.popup button {
    background-color: #008CBA; /* لون زر الشراء */
    color: white; /* لون النص في الزر */
    padding: 10px 20px; /* حشوة داخل الزر */
    border: none; /* إزالة الحدود */
    border-radius: 5px; /* زوايا دائرية للزر */
    cursor: pointer;
    font-size: 18px;
    display: block;
    margin: 20px auto 0; /* توسيط الزر */
}

.popup button:hover {
    background-color: #005f73; /* لون عند مرور المؤشر */
}


    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <h1 id="priceInHand">سعرك بيدك</h1>
                </button>
              <div class="header-controls">
                <div class="search-container">
                    <i class="fas fa-search search-icon" onclick="toggleSearch()"></i>
                    <input type="text" id="searchInput" placeholder="البحث عن المنتجات...">
                </div>
                <div id="ad-banner"></div>
                <button class="header-button dark-mode-toggle" onclick="toggleDarkMode()">
                    <i class="fas fa-moon"></i>
                </button>
                <button class="header-button language-toggle" onclick="toggleLanguage()">EN</button>
                
            </div>
       <!-- قائمة التصنيفات مع التحسينات -->
<select id="categorySelect" class="custom-select" onchange="filterProductsByCategory()">
    <option value="">اختر التصنيف</option>
    <option value="men-clothing">ملابس رجالي</option>
    <option value="kids-clothing">ملابس أطفال</option>
    <option value="women-clothing">ملابس نسائي</option>
    <option value="women-shoes">أحذية نسائي</option>
    <option value="men-shoes">أحذية رجالي</option>
    <option value="kids-suits">بدلات أطفال</option>
    <option value="men-suits">بدلات رجالي</option>
    <option value="women-suits">بدلات نسائي</option>
    <option value="cosmetics">كوزمتك</option>
    <option value="scarves">شالات</option>
    <option value="school-clothing">ملابس مدرسية</option>
    <option value="bodysuits">بديات</option>
    <option value="t-shirts">تيشرتات</option>
    <option value="men-pants">بنطلون رجالي</option>
    <option value="jeans">بنطلون جينز</option>
    <option value="pants-12">بنطلون 12</option>
    <option value="women-pants">بنطلون نسائي</option>
    <option value="women-bodysuits">بديات نسائي</option>
    <option value="women-tshirts">تيشرتات نسائي</option>
    <option value="bras">صدريات</option>
    <option value="dresses">فساتين</option>
    <option value="underwear">ملابس داخلية</option>
    <option value="sleepwear-sets">سيتات نوم</option>
    <option value="hair-dyes">أصبغ شعر</option>
    <option value="shampoos">شامبوات</option>
    <option value="makeup">مكياج</option>
    <option value="perfumes">عطور</option>
    <option value="sports-shoes">أحذية رياضية</option>
    <option value="trench-shoes">أحذية ترانشوز</option>
    <option value="formal-shoes">أحذية رسمية</option>
    <option value="formal-shirts">قمصان رسمية</option>
    <option value="jackets">كباري</option>
    <option value="youth-shirts">قمصان شبابية</option>
    <option value="classic-clothing">كلاسيك</option>
    <option value="miscellaneous">تصنيفات متنوعة</option>
</select>
  </div>
  

    <div id="story-modal">
        <span id=""إ;</span>
    </div>



         <div class="floating-info">
                <div class="digital-clock" id="clock">
                    <span class="flip-card" id="hours">00</span>:
                    <span class="flip-card" id="minutes">00</span>:
                    <span class="flip-card" id="seconds">00</span>
                </div>
            
                </div>

       <div class="subscriber-count">
    المشاهدات: <span class="flip-card" id="views">0</span>
</div>


                  
            </div>
       
        </div>
        <div class="products-grid" id="likesContainer">
    <!-- Liked items will be dynamically loaded here -->
</div>
 


    </div>
    <div id="mySidebar" class="sidebar">
        <div class="user-info" id="userInfo">
            <img id="userAvatar" src="https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737" alt="User Avatar" style="border-radius: 50%; width: 50px; height: 50px;">
            <span id="userName">     1995-1-1-110-</span>
        </div>
        
        <a href="javascript:void(0)" class="closebtn" onclick="closeSidebar()">&times;</a>
        <a href="#" onclick="fetchProducts()"><i class="fas fa-home sidebar-icon"></i> الرئيسية</a>
        <a href="#" onclick="showLikedProducts()"><i class="fas fa-heart sidebar-icon"></i> الإعجابات</a>
        <a href="#" onclick="showFavoriteProducts()"><i class="fas fa-star sidebar-icon"></i> المفضلة</a>
        <a href="#" onclick="showSavedProducts()"><i class="fas fa-bookmark sidebar-icon"></i> المحفوظات</a>
        <a href="#" onclick="showCategories()"><i class="fas fa-list sidebar-icon"></i> التصنيفات</a>
        <a href="#" onclick="showOffers()"><i class="fas fa-percentage sidebar-icon"></i> العروض</a>
        
    </div>
   

    </div>:
    
    <div class="bottom-navbar">
        <a href="#" onclick="fetchProducts()" class="nav-item">
            <i class="fas fa-home"></i>
            <span>الرئيسية</span>
        </a>
        <a href="#" onclick="showLikedProducts()" class="nav-item">
            <i class="fas fa-heart"></i>
            <span>الإعجابات</span>
        </a>
        <a href="#" onclick="showFavoriteProducts()" class="nav-item">
            <i class="fas fa-star"></i>
            <span>المفضلة</span>
        </a>
        <a href="#" onclick="showSavedProducts()" class="nav-item">
            <i class="fas fa-bookmark"></i>
            <span>المحفوظات</span>
        </a>
        <a href="#" onclick="showCategories()" class="nav-item">
            <i class="fas fa-list"></i>
            <span>التصنيفات</span>
        </a>
        <a href="#" onclick="showOffers()" class="nav-item">
            <i class="fas fa-percentage"></i>
            <span>العروض</span>
        </a>
    </div>
    
    <div id="pricePopup" class="popup">
        <h3>جاري تحديد السعر الخاص بك...</h3>
        <div id="countdown" class="timer">3</div>
        <div id="randomPrice" class="price-display">---</div>
        <button onclick="closePopup()">إغلاق</button>
        <button id="addToCartBtn" onclick="addToCart()" style="display: none;">إضافة إلى السلة</button>
    </div>

    
    <div class="add-product-form" id="addProductForm">
    <h3>إضافة منتج جديد</h3>
    <input type="text" id="newProductName" placeholder="اسم المنتج">
    <input type="file" id="newProductImage" accept="image/*" multiple>
    <input type="number" id="newProductPriceOriginal" placeholder="السعر الأصلي">
    <input type="number" id="newProductPriceDiscount" placeholder="سعر الخصم">
    <input type="number" id="newProductPriceSuperDiscount" placeholder="سعر الخصم الفائق">
    <input type="text" id="newProductFileName" placeholder="اسم ملف الصفحة (HTML)">
   <input type="number" id="newProductQuantity" placeholder="الكمية المتوفرة">

     <select id="newProductCategory" class="custom-select">
        <option value="">اختر التصنيف</option>
    <option value="men-clothing">ملابس رجالي</option>
    <option value="kids-clothing">ملابس أطفال</option>
    <option value="women-clothing">ملابس نسائي</option>
    <option value="women-shoes">أحذية نسائي</option>
    <option value="men-shoes">أحذية رجالي</option>
    <option value="kids-suits">بدلات أطفال</option>
    <option value="men-suits">بدلات رجالي</option>
    <option value="women-suits">بدلات نسائي</option>
    <option value="cosmetics">كوزمتك</option>
    <option value="scarves">شالات</option>
    <option value="school-clothing">ملابس مدرسية</option>
    <option value="bodysuits">بديات</option>
    <option value="t-shirts">تيشرتات</option>
    <option value="men-suits">بدلات رجالي</option>
    <option value="men-pants">بنطلون رجالي</option>
    <option value="jeans">بنطلون جينز</option>
    <option value="pants-12">بنطلون 12</option>
    <option value="women-pants">بنطلون نسائي</option>
    <option value="women-bodysuits">بديات نسائي</option>
    <option value="women-tshirts">تيشرتات نسائي</option>
    <option value="bras">صدريات</option>
    <option value="dresses">فساتين</option>
    <option value="underwear">ملابس داخلية</option>
    <option value="sleepwear-sets">سيتات نوم</option>
    <option value="hair-dyes">أصبغ شعر</option>
    <option value="shampoos">شامبوات</option>
    <option value="makeup">مكياج</option>
    <option value="perfumes">عطور</option>
    <option value="sports-shoes">أحذية رياضية</option>
    <option value="trench-shoes">أحذية ترانشوز</option>
    <option value="formal-shoes">أحذية رسمية</option>
    <option value="formal-shirts">قمصان رسمية</option>
    <option value="jackets">كباري</option>
    <option value="youth-shirts">قمصان شبابية</option>
    <option value="classic-clothing">كلاسيك</option>
    <option value="miscellaneous">تصنيفات متنوعة</option>
</select>

        <button onclick="addProduct()">إضافة المنتج</button>
        
   
        </div>
           
    

    <!-- نافذة منبثقة لإضافة إعلان -->
    <div id="adPopup" class="popup">
        <h3>إضافة إعلان جديد</h3>
        <input type="text" id="adName" placeholder="اسم الإعلان">
        <input type="file" id="adImage" accept="image/*">
        <input type="text" id="adPage" placeholder="اسم الصفحة (HTML)">
        <button onclick="uploadAd()">رفع الإعلان</button>
        <button onclick="closeAdPopup()">إغلاق</button>
    </div>

    <!-- الشريط الإعلاني -->
    <div class="carousel" id="adCarousel">
        <!-- سيتم إضافة الصور ديناميكيًا هنا -->
    </div>
    </div>

    <!-- المنتجات -->
    <div class="products" id="products">
        <!-- المنتجات ستظهر هنا -->
    </div>
</body>
                    
   <!-- الزر الرئيسي المنبثق (أيقونة الإضافة) -->
<button class="popup-toggle" onclick="toggleMenu()">
<i class="fas fa-plus"></i>

  </button>
    
    
</button>

<!-- قائمة الأزرار المنبثقة -->
<div id="popupMenu" class="popup-menu">
  <!-- أيقونات القائمة -->
  <button class="menu-item" onclick="openAdPopup()">
    <i class="fas fa-bullhorn"></i>
  </button>

  <button class="menu-item" onclick="redirectToCartPage()">
    <i class="fas fa-shopping-cart"></i>
    <span class="cart-count" id="cartCount">0</span>
  </button>

  <button class="menu-item" onclick="toggleAddProductForm()">
    <i class="fas fa-box"></i>
  </button>

  <button class="menu-item" onclick="redirectToMessagesPage()">
    <i class="fas fa-envelope"></i>
    <span id="messageCount" 
</div>


    
    </div>
<div id="popup" class="popup" style="display:none;">
    <h2>أدخل الرمز التعريفي الخاص بك</h2>
    <input type="text" id="userCode" placeholder="الرمز التعريفي">
    <button onclick="verifyCode()">إرسال</button>
    <button onclick="contactAdmin()">  احصل على الرمز</button>
</div>

<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-database.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-storage.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-auth.js"></script>
<script>
    const firebaseConfig = {
        apiKey: "AIzaSyDGpAHia_wEmrhnmYjrPf1n1TrAzwEMiAI",
        authDomain: "messageemeapp.firebaseapp.com",
        databaseURL: "https://messageemeapp-default-rtdb.firebaseio.com",
        projectId: "messageemeapp",
        storageBucket: "messageemeapp.appspot.com",
        messagingSenderId: "255034474844",
        appId: "1:255034474844:web:5e3b7a6bc4b2fb94cc4199"
    };
    firebase.initializeApp(firebaseConfig);
    const auth = firebase.auth();
    const database = firebase.database();
    const storage = firebase.storage();

   // تتبع عدد مرات فتح التطبيق
let openCount = parseInt(localStorage.getItem('openCount')) || 0; // تحويل القيمة إلى رقم
openCount++;
localStorage.setItem('openCount', openCount);

// إذا تم فتح التطبيق أكثر من 5 مرات، أظهر النافذة المنبثقة
if (openCount > 5) {
    showPopup();
}

    // إنشاء معرف فريد لكل مستخدم
    let userId = localStorage.getItem('userId');
    if (!userId) {
        userId = 'user_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('userId', userId);
        // حفظ المعرف في Firebase
        firebase.database().ref('users/' + userId).set({ id: userId });
    }

    // توليد رقم عشوائي ثابت إذا لم يكن موجودًا بالفعل في قاعدة البيانات
    function generateAndSaveRandomCode() {
        firebase.database().ref('users/' + userId).once('value').then(function(snapshot) {
            const data = snapshot.val();
            if (!data.randomCode) {
                // إذا لم يكن الرمز العشوائي موجودًا، أنشئ رمزًا جديدًا واحفظه
                const randomCode = Math.floor(100000 + Math.random() * 900000); // إنشاء رقم مكون من 6 أرقام عشوائية
                firebase.database().ref('users/' + userId).update({ randomCode: randomCode });
            }
        });
    }

    // إرسال رسالة ترحيب فقط عبر واتساب عند النقر على زر "التواصل مع المسؤول"
    function contactAdmin() {
        // استدعاء دالة إنشاء وحفظ الرمز العشوائي إذا لم يكن موجودًا
        generateAndSaveRandomCode();

        // إرسال رسالة ترحيب فقط إلى المسؤول عبر واتساب
        const whatsappNumber = '9647813798636'; // رقم واتساب المسؤول
        const message = `مرحبًا!    .   .`;
        const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
        window.location.href = whatsappUrl; // فتح رابط واتساب وإرسال الرسالة
    }

    // إظهار النافذة المنبثقة لطلب الرمز التعريفي
    function showPopup() {
        // تحقق مما إذا تم إدخال الرمز مسبقًا
        if (!localStorage.getItem('isCodeVerified')) {
            document.getElementById('popup').style.display = 'block';
        }
    }

    // التحقق من الرمز التعريفي الذي تم إدخاله من قاعدة البيانات
    function verifyCode() {
        const enteredCode = document.getElementById('userCode').value;

        // التحقق من الرمز العشوائي من قاعدة بيانات Firebase
        firebase.database().ref('users/' + userId).once('value').then(function(snapshot) {
            const storedRandomCode = snapshot.val().randomCode;

            // التحقق من الرمز المدخل
            if (enteredCode === storedRandomCode.toString()) {
                alert('تم التحقق بنجاح! يمكنك المتابعة.');
                document.getElementById('popup').style.display = 'none'; // إخفاء النافذة المنبثقة
                localStorage.setItem('isCodeVerified', true); // تخزين الحالة كتم التحقق
                openApp(); // فتح التطبيق بصورة طبيعية
            } else {
                alert('الرمز غير صحيح. حاول مرة أخرى.');
            }
        });
    }

    // فتح التطبيق بعد التحقق
    function openApp() {
        // هنا يمكنك تنفيذ ما تراه مناسبًا لفتح التطبيق بشكل طبيعي
        // على سبيل المثال: إعادة توجيه المستخدم إلى الصفحة الرئيسية أو إزالة القيود
        window.location.href = 'product-details.html'; // إعادة توجيه المستخدم إلى الصفحة الرئيسية
    }

    // عرض النافذة المنبثقة إذا كانت الحالة غير متحققة
    showPopup();











    // إعدادات أخرى متعلقة بالتطبيق
    let currentLanguage = 'ar';
    let isDarkMode = false;
    let currentProductId = null;
    let currentPrice = null;
    
    let stories = [];
    let currentStoryIndex = 0;

    // تحميل القصص من قاعدة البيانات
    function loadStories() {
        const container = document.getElementById('stories-container');
        container.innerHTML = '';
        stories = [];

        const addStoryElement = document.createElement('div');
        addStoryElement.className = 'add-story';
        addStoryElement.innerHTML = `
            <div class="add-story-content">+</div>
            <p>إضافة قصة</p>
        `;
        container.appendChild(addStoryElement);
        addStoryElement.addEventListener('click', addStory);

        // استرجاع القصص من قاعدة البيانات
        firebase.database().ref('stories/' + userId).once('value', (snapshot) => {
            snapshot.forEach((childSnapshot) => {
                const storyData = childSnapshot.val();
                const storyElement = document.createElement('div');
                storyElement.className = 'story';
                storyElement.dataset.video = storyData.videoUrl;
                storyElement.innerHTML = `
                    <div class="story-border"></div>
                    <div class="story-content">
                        <video src="${storyData.videoUrl}" muted loop playsinline></video>
                    </div>
                    <p>قصتك</p>
                `;
                container.appendChild(storyElement);
                stories.push({ url: storyData.videoUrl });

                storyElement.addEventListener('click', () => openStoryModal(stories.length - 1));
            });
        });
    }



/// دالة لفتح وإغلاق القائمة المنبثقة عند النقر على الزر
let firstClick = true; // متغير لتتبع النقرات

// دالة لفتح وإغلاق القائمة المنبثقة عند النقر على الزر
function toggleMenu() {
  const popupMenu = document.getElementById("popupMenu");
  popupMenu.style.display = popupMenu.style.display === "flex" ? "none" : "flex";
}

// إضافة مستمعين للأيقونات في القائمة المنبثقة
document.addEventListener("DOMContentLoaded", function() {
  const menuItems = document.querySelectorAll('.menu-item');

  menuItems.forEach(item => {
    item.addEventListener('click', function(event) {
      if (firstClick) {
        event.preventDefault(); // منع الانتقال في النقرة الأولى
        firstClick = false; // تعيين النقر الثاني
      } else {
        firstClick = true; // إعادة تعيين النقر بعد الثانية
        // تنفيذ الإجراء هنا (الانتقال للصفحة المطلوبة)
        this.click(); // إجراء النقر الثاني
      }
    });
  });
});


// فتح النافذة المنبثقة لإضافة الإعلان
function openAdPopup() {
    document.getElementById('adPopup').style.display = 'block';
}

// إغلاق النافذة المنبثقة
function closeAdPopup() {
    document.getElementById('adPopup').style.display = 'none';
}

// دالة لرفع الإعلان إلى Firebase
function uploadAd() {
    const adName = document.getElementById('adName').value;
    const adPage = document.getElementById('adPage').value;
    const adImage = document.getElementById('adImage').files[0];

    if (!adName || !adPage || !adImage) {
        alert('يرجى تعبئة جميع الحقول!');
        return;
    }

    const storageRef = firebase.storage().ref('ad1/' + adImage.name); // المسار ad1
    const uploadTask = storageRef.put(adImage);

    uploadTask.on('state_changed', 
        function(snapshot) {}, 
        function(error) {
            console.error('حدث خطأ أثناء رفع الصورة:', error);
        }, 
        function() {
            uploadTask.snapshot.ref.getDownloadURL().then(function(downloadURL) {
                const adData = {
                    name: adName,
                    imageUrl: downloadURL,
                    pageUrl: adPage,
                    timestamp: Date.now()
                };

                const adRef = firebase.database().ref('ad1'); // المسار ad1
                adRef.push(adData).then(() => {
                    alert('تم رفع الإعلان بنجاح!');
                    closeAdPopup(); // إغلاق النافذة بعد الرفع
                    fetchAds(); // تحديث الشريط الإعلاني
                }).catch((error) => {
                    console.error('حدث خطأ أثناء حفظ بيانات الإعلان:', error);
                });
            });
        }
    );
}

// دالة لجلب الإعلانات وعرضها في الشريط الإعلاني
function fetchAds() {
    const adRef = firebase.database().ref('ad1').orderByChild('timestamp'); // المسار ad1
    const carousel = document.getElementById('adCarousel');

    // استرجاع الإعلانات من قاعدة البيانات
    adRef.on('value', (snapshot) => {
        const ads = snapshot.val();
        if (ads) {
            carousel.innerHTML = '';  // مسح الصور السابقة

            let isFirst = true;
            for (let key in ads) {
                const ad = ads[key];
                const imgElement = document.createElement('img');
                imgElement.src = ad.imageUrl;
                imgElement.alt = ad.name;
                imgElement.setAttribute('data-url', ad.pageUrl);

                // إضافة الفئة "active" للصورة الأولى فقط
                if (isFirst) {
                    imgElement.classList.add('active');
                    isFirst = false;
                }

                carousel.appendChild(imgElement);

                // إضافة حدث النقر لنقل المستخدم إلى الصفحة المحددة
                imgElement.addEventListener('click', () => {
                    window.location.href = ad.pageUrl;
                });
            }

            // بعد عرض الإعلانات، تفعيل الحركة التلقائية للـ carousel
            initializeCarousel();
        }
    });
}

// دالة لتحريك الـ carousel تلقائيًا
function initializeCarousel() {
    const images = document.querySelectorAll('.carousel img');
    let currentIndex = 0;

    setInterval(() => {
        images[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].classList.add('active');
    }, 5000); // تغيير الصورة كل 5 ثواني
}

// التأكد من استدعاء دالة fetchAds عند تحميل الصفحة
window.addEventListener('load', () => {
    fetchAds(); // استدعاء الدالة لجلب الإعلانات وعرضها فور تحميل الصفحة
});
    



        function toggleDarkMode() {
            isDarkMode = !isDarkMode;
            document.body.classList.toggle('dark-mode', isDarkMode);
            const darkModeToggle = document.querySelector('.dark-mode-toggle i');
            darkModeToggle.className = isDarkMode ? 'fas fa-sun' : 'fas fa-moon';
        }

        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                localStorage.setItem('userId', user.uid);
                updateLoginUI(); // تحديث واجهة المستخدم بعد تسجيل الدخول
            } else {
                // في حالة عدم وجود جلسة مستخدم مسجلة
                showLoginPopup();
            }
        });
        function formatViews(views) {
    if (views >= 1000000) {
        return (views / 1000000).toFixed(1) + 'M'; // إذا كان عدد المشاهدات بالملايين
    } else if (views >= 1000) {
        return (views / 1000).toFixed(1) + 'K'; // إذا كان عدد المشاهدات بالآلاف
    } else {
        return views.toString(); // إذا كان العدد أقل من 1000 يعرض العدد كما هو
    }
}

// تحديث عدد المشاهدات ديناميكيًا
function updateViewsCount(views) {
    const viewsElement = document.getElementById('views');
    viewsElement.textContent = formatViews(views);
}

// مثال على استدعاء الدالة مع عدد مشاهدات كبير
let viewsCount = 120000; // يمكنك جلب هذا العدد من قاعدة البيانات أو أي مصدر آخر
updateViewsCount(viewsCount);

      // Function to redirect to the Messages HTML page
// عند تحميل الصفحة الرئيسية، جلب عدد الرسائل من قاعدة البيانات
function fetchMessageCount() {
    const messageCountRef = firebase.database().ref('messageCount/counter');
    
    messageCountRef.on('value', function(snapshot) {
        const count = snapshot.val() || 0; // الحصول على العدد أو استخدام 0 إذا لم يكن موجودًا
        document.getElementById('messageCount').textContent = count; // تحديث العداد في الواجهة
    });
}
// Function to redirect to the Messages HTML page
function redirectToMessagesPage() {
    window.location.href = 'messages.html'; // Replace with your actual messages HTML file path
}


// استدعاء الدالة عند تحميل الصفحة الرئيسية
window.onload = fetchMessageCount;

  
        
        function logout() {
            firebase.auth().signOut().then(function() {
                localStorage.removeItem('userId');
                window.location.reload(); // إعادة تحميل الصفحة بعد تسجيل الخروج
            }).catch(function(error) {
                console.error('Error signing out:', error);
            });
        }
        

        function showLoginPopup() {
            document.getElementById("loginPopup").style.display = "flex";
        }
        
        function hideLoginPopup() {
            document.getElementById("loginPopup").style.display = "none";
        }
        function loginWithEmail() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            firebase.auth().signInWithEmailAndPassword(email, password)
                .then((userCredential) => {
                    const user = userCredential.user;
                    localStorage.setItem('userId', user.uid);
                    localStorage.setItem('userImage', user.photoURL || 'https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737');
                    hideLoginPopup();
                    updateLoginUI();
                })
                .catch((error) => {
                    alert('Login Failed: ' + error.message);
                });
        }
        function loginWithGoogle() {
            const provider = new firebase.auth.GoogleAuthProvider();
            firebase.auth().signInWithPopup(provider)
                .then((result) => {
                    const user = result.user;
                    localStorage.setItem('userId', user.uid);
                    localStorage.setItem('userImage', user.photoURL || 'default-profile.png');
                    hideLoginPopup();
                    updateLoginUI();
                })
                .catch((error) => {
                    console.error('Login Failed:', error);
                });
        }function updateLoginUI() {
            const userId = localStorage.getItem('userId');
            const userImage = localStorage.getItem('userImage') || 'default-profile.png';
        
            if (userId) {
                document.querySelector('.login-button').style.display = 'none';
                const profileImg = document.createElement('img');
                profileImg.src = userImage;
                profileImg.alt = 'Profile Image';
                profileImg.style.width = '50px';
                profileImg.style.height = '50px';
                document.querySelector('.subscriber-count').appendChild(profileImg);
            }
        }
        
        

        function toggleLanguage() {
            currentLanguage = currentLanguage === 'ar' ? 'en' : 'ar';
            document.documentElement.lang = currentLanguage;
            document.documentElement.dir = currentLanguage === 'ar' ? 'rtl' : 'ltr';
            updateLanguage();
        }

        // Add this new function to handle adding items to cart
        function toggleCart(productId) {
            const productRef = database.ref('products/' + productId + '/cart/' + userId);
            productRef.once('value').then((snapshot) => {
                if (snapshot.val()) {
                    productRef.remove();
                } else {
                    productRef.set(true);
                }
                updateCartCount();
            });
        }
        // Add this new function to update the cart count
        function updateCartCount() {
            const cartCountElement = document.getElementById('cartCount');
            database.ref('carts/' + userId).once('value', (snapshot) => {
                const cart = snapshot.val();
                const count = cart ? Object.keys(cart).length : 0;
                cartCountElement.textContent = count;
            });
        }
        // Add this new function to show cart items
        function showCart() {
            const productsContainer = document.getElementById('products');
            productsContainer.innerHTML = '<h2>سلة التسوق</h2>';
            database.ref('carts/' + userId).once('value', (snapshot) => {
                const cart = snapshot.val();
                if (cart) {
                    for (let productId in cart) {
                        const productCard = createCartItemCard(productId, cart[productId]);
                        productsContainer.innerHTML += productCard;
                    }
                    productsContainer.innerHTML += `
                <button id="checkoutButton" class="buy-button" onclick="goToCheckout()">
                    إتمام الشراء
                </button>
            `;
                } else {
                    productsContainer.innerHTML += '<p>السلة فارغة</p>';
                }
            });
        }

        // الدالة التي تنقل المستخدم إلى صفحة الخروج (Checkout)
function goToCheckout() {
    window.location.href = 'checkout.html';
}

// الدالة التي تنشئ بطاقة عنصر المنتج في السلة
function createCartItemCard(productId, product) {
    return `
        <div class="product-card" data-product-id="${productId}">
            <!-- قسم الصور للمنتج -->
            <div class="product-images">
                <img src="${product.images[0]}" alt="${product.name}" class="product-image" style="width: 350px; height: 350px;">
            </div>
            <!-- قسم المعلومات عن المنتج -->
            <div class="product-info">
                <h3>${product.name}</h3>
                <!-- عرض السعر المختار -->
                <p class="price">السعر المختار: $${product.price.toFixed(2)}</p>
                <!-- عرض السعر الأصلي -->
                <p class="price">السعر الأصلي: $${product.priceOriginal}</p>
                <!-- عرض سعر الخصم -->
                <p class="price">سعر الخصم: $${product.priceDiscount}</p>
                <!-- عرض سعر الخصم الفائق -->
                <p class="price">سعر الخصم الفائق: $${product.priceSuperDiscount}</p>
                <!-- زر لإزالة المنتج من السلة -->
                <button class="action-button" onclick="removeFromCart('${productId}')">
                    <i class="fas fa-trash"></i> إزالة من السلة
                </button>
            </div>
        </div>
    `;
}

// الدالة التي تقوم بإزالة المنتج من السلة
function removeFromCart(productId) {
    // الوصول إلى قاعدة البيانات Firebase وإزالة المنتج من سلة المستخدم
    database.ref('carts/' + userId + '/' + productId).remove()
        .then(() => {
            // عرض رسالة تأكيد للمستخدم عند نجاح إزالة المنتج
            alert('تم إزالة المنتج من السلة بنجاح!');
            // تحديث عرض السلة بعد إزالة المنتج
            showCart();
            // تحديث عدد المنتجات في السلة
            updateCartCount();
        })
        .catch((error) => {
            // عرض رسالة خطأ في حال حدث مشكلة أثناء إزالة المنتج
            alert('حدث خطأ أثناء إزالة المنتج من السلة.');
        });
}

// التحكم في قياسات العناصر
let fontSize = 16; // حجم الخط الافتراضي
let cardSize = 300; // حجم البطاقة الافتراضي

// دالة لتغيير حجم الخط
function changeFontSize(change) {
    fontSize += change;
    document.body.style.fontSize = `${fontSize}px`;
    updateProductCards();
}

// دالة لتغيير حجم بطاقات المنتجات
function changeCardSize(change) {
    cardSize += change;
    updateProductCards();
}

// دالة لتحديث بطاقات المنتجات
function updateProductCards() {
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.style.width = `${cardSize}px`;
        card.style.height = `${cardSize * 5.1}px`; // نسبة الارتفاع إلى العرض 1.5
    });
}

// دالة لإنشاء أزرار التحكم في الحجم
function createSizeControls() {
    const controlsContainer = document.createElement('div');
    controlsContainer.className = 'size-controls';
    controlsContainer.innerHTML = `
        <button onclick="changeFontSize(1)">زيادة حجم الخط</button>
        <button onclick="changeFontSize(-1)">تقليل حجم الخط</button>
        <button onclick="changeCardSize(10)">زيادة حجم البطاقة</button>
        <button onclick="changeCardSize(-10)">تقليل حجم البطاقة</button>
    `;
    document.body.insertBefore(controlsContainer, document.body.firstChild);
}

// تحديث دالة createProductCard لتطبيق الأحجام الجديدة
function createProductCard(key, product) {
    // ... (الكود السابق)

    const cardHtml = `
        <div class="product-card" data-product-id="${key}" style="width: ${cardSize}px; height: ${cardSize * 1.5}px;">
            <!-- ... (باقي محتوى البطاقة) -->
        </div>
    `;

    return cardHtml;
}

// تحديث دالة fetchProducts لتطبيق التغييرات على البطاقات الجديدة
function fetchProducts() {
    // ... (الكود السابق)

    database.ref('products').on('value', (snapshot) => {
        const products = snapshot.val();
        productsContainer.innerHTML = '';
        for (let key in products) {
            const product = products[key];
            const productCard = createProductCard(key, product);
            productsContainer.innerHTML += productCard;
        }
        initializeImageSliders();
        updateCartCount();
        updateProductCards(); // تطبيق الأحجام الجديدة
    });
}

// تحديث دالة window.onload لإضافة أزرار التحكم في الحجم
window.onload = () => {
    fetchProducts();
    updateLanguage();
    updateCartCount();
    createSizeControls();
    
    fetchProduc
    
    updateCartCount();
};

// ... (باقي الكود السابق)

        

        function updateLanguage() {
            const translations = {
                ar: {
                    title: 'المتجر الحديث المطور',
                    search: 'البحث عن المنتجات...',
                    home: 'الرئيسية',
                    likes: 'الإعجابات',
                    favorites: 'المفضلة',
                    saved: 'المحفوظات',
                    categories: 'التصنيفات',
                    offers: 'العروض',
                    addProduct: 'إضافة منتج جديد',
                    productName: 'اسم المنتج',
                    originalPrice: 'السعر الأصلي',
                    discountPrice: 'سعر الخصم',
                    superDiscountPrice: 'سعر الخصم الفائق',
                    category: 'اختر التصنيف',
                    add: 'إضافة المنتج',
                    determiningPrice: 'جاري تحديد السعر الخاص بك...',
                    close: 'إغلاق',
                    buyNow: 'شراء الآن',
                    languageToggle: 'English'
                },
                en: {
                    title: 'Advanced Modern Store',
                    search: 'Search for products...',
                    home: 'Home',
                    likes: 'Likes',
                    favorites: 'Favorites',
                    saved: 'Saved',
                    categories: 'Categories',
                    offers: 'Offers',
                    addProduct: 'Add New Product',
                    productName: 'Product Name',
                    originalPrice: 'Original Price',
                    discountPrice: 'Discount Price',
                    superDiscountPrice: 'Super Discount Price',
                    category: 'Choose Category',
                    add: 'Add Product',
                    determiningPrice: 'Determining Your Price...',
                    close: 'Close',
                    buyNow: 'Buy Now',
                    languageToggle: 'العربية'
                }
            };

            document.querySelector('.header h1').textContent = translations[currentLanguage].title;
            document.getElementById('searchInput').placeholder = translations[currentLanguage].search;
            document.querySelectorAll('.sidebar a')[1].innerHTML = `<i class="fas fa-home"></i> ${translations[currentLanguage].home}`;
            document.querySelectorAll('.sidebar a')[2].innerHTML = `<i class="fas fa-heart"></i> ${translations[currentLanguage].likes}`;
            document.querySelectorAll('.sidebar a')[3].innerHTML = `<i class="fas fa-star"></i> ${translations[currentLanguage].favorites}`;
            document.querySelectorAll('.sidebar a')[4].innerHTML = `<i class="fas fa-bookmark"></i> ${translations[currentLanguage].saved}`;
            document.querySelectorAll('.sidebar a')[5].innerHTML = `<i class="fas fa-list"></i> ${translations[currentLanguage].categories}`;
            document.querySelectorAll('.sidebar a')[6].innerHTML = `<i class="fas fa-percentage"></i> ${translations[currentLanguage].offers}`;
            document.querySelector('#addProductForm h3').textContent = translations[currentLanguage].addProduct;
            document.getElementById('newProductName').placeholder = translations[currentLanguage].productName;
            document.getElementById('newProductPriceOriginal').placeholder = translations[currentLanguage].originalPrice;
            document.getElementById('newProductPriceDiscount').placeholder = translations[currentLanguage].discountPrice;
            document.getElementById('newProductPriceSuperDiscount').placeholder = translations[currentLanguage].superDiscountPrice;
            document.getElementById('newProductCategory').options[0].text = translations[currentLanguage].category;
            document.querySelector('#addProductForm button').textContent = translations[currentLanguage].add;
            document.querySelector('#pricePopup h3').textContent = translations[currentLanguage].determiningPrice;
            document.querySelector('#pricePopup button').textContent = translations[currentLanguage].close;
            document.getElementById('purchaseButton').textContent = translations[currentLanguage].buyNow;
            document.querySelector('.language-toggle').textContent = translations[currentLanguage].languageToggle;

            fetchProducts();
        }

        function openSidebar() {
            document.getElementById("mySidebar").style.width = "200px";
        }

        function closeSidebar() {
            document.getElementById("mySidebar").style.width = "0";
        }

        // Update the fetchProducts function to also update the cart count
       function createProductCard(key, product) {
    const images = product.images || [product.image];
    const imagesHtml = images.map((img, index) => `
        <img src="${img}" alt="${product.name}" class="product-image" style="opacity: ${index === 0 ? 1 : 0};" onclick="redirectToProductPage('${product.fileName}')">
    `).join('');

    // Check if the product is out of stock
    const isOutOfStock = product.quantity <= 0;

    return `
        <div class="product-card" data-product-id="${key}">
            <div class="product-images">
                ${imagesHtml}
                <button class="image-nav prev" onclick="changeImage('${key}', -1)">❮</button>
                <button class="image-nav next" onclick="changeImage('${key}', 1)">❯</button>
            </div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p class="price">السعر الأصلي: $${product.priceOriginal}</p>
                <p class="price">سعر الخصم: $${product.priceDiscount}</p>
                <p class="price">سعر الخصم الفائق: $${product.priceSuperDiscount}</p>
                  <!-- Update stock quantity with larger font and custom color -->
                <p class="stock" style="color: #ff5733; font-size: 1.0rem; font-weight: bold;">
                    الكمية المتوفرة: ${product.quantity}
                </p>

                <div class="action-buttons">
                    <button class="action-button" onclick="toggleLike('${key}')">
                        <i class="fas fa-heart ${product.likes && product.likes[userId] ? 'text-danger' : ''}"></i>
                        <span class="action-count">${countObjectProperties(product.likes)}</span>
                    </button>
                    <button class="action-button" onclick="toggleFavorite('${key}')">
                        <i class="fas fa-star ${product.favorites && product.favorites[userId] ? 'text-warning' : ''}"></i>
                        <span class="action-count">${countObjectProperties(product.favorites)}</span>
                    </button>
                    <button class="action-button" onclick="toggleSave('${key}')">
                        <i class="fas fa-bookmark ${product.saved && product.saved[userId] ? 'text-primary' : ''}"></i>
                        <span class="action-count">${countObjectProperties(product.saved)}</span>
                    </button>
                    <button class="action-button" onclick="toggleCart('${key}')">
                        <i class="fas fa-shopping-cart ${product.cart && product.cart[userId] ? 'text-success' : ''}"></i>
                        <span class="action-count">${countObjectProperties(product.cart)}</span>
                    </button>
                </div>

                <!-- Show "Buy" button if the product is in stock, otherwise hide it -->
                <button class="buy-button" ${isOutOfStock ? 'style="display:none;"' : ''} onclick="showPricePopup('${key}')">
                    شراء الآن
                </button>
            </div>
        </div>
    `;
}


// دالة لإعادة التوجيه إلى صفحة المنتج
function redirectToProductPage(fileName) {
    if (fileName) {
        window.location.href = fileName; // الانتقال إلى صفحة HTML المرتبطة بالمنتج
    } else {
        alert('لا يوجد ملف مرتبط بهذا المنتج.');
    }
}


// دالة لإعادة التوجيه إلى صفحة المنتج
function redirectToProductPage(fileName) {
    if (fileName) {
        window.location.href = fileName; // الانتقال إلى صفحة HTML المرتبطة بالمنتج
    } else {
        alert('لا يوجد ملف مرتبط بهذا المنتج.');
    }
}






// تحديث دوال التفاعلات لإيقاف الحدث ومنع التداخل
function toggleLike(key, event) {
    event.stopPropagation();  // إيقاف التداخل
    const productRef = database.ref('products/' + key + '/likes/' + userId);
    productRef.once('value').then((snapshot) => {
        if (snapshot.val()) {
            productRef.remove();
        } else {
            productRef.set(true);
        }
    });
}

function toggleFavorite(key, event) {
    event.stopPropagation();  // إيقاف التداخل
    const productRef = database.ref('products/' + key + '/favorites/' + userId);
    productRef.once('value').then((snapshot) => {
        if (snapshot.val()) {
            productRef.remove();
        } else {
            productRef.set(true);
        }
    });
}

function toggleSave(key, event) {
    event.stopPropagation();  // إيقاف التداخل
    const productRef = database.ref('products/' + key + '/saved/' + userId);
    productRef.once('value').then((snapshot) => {
        if (snapshot.val()) {
            productRef.remove();
        } else {
            productRef.set(true);
        }
    });
}

function toggleCart(key, event) {
    event.stopPropagation();  // إيقاف التداخل
    const productRef = database.ref('products/' + key + '/cart/' + userId);
    productRef.once('value').then((snapshot) => {
        if (snapshot.val()) {
            productRef.remove();
        } else {
            productRef.set(true);
        }
    });
}



        function countObjectProperties(obj) {
            return obj ? Object.keys(obj).length : 0;
        }

        function changeImage(productId, direction) {
            const productCard = document.querySelector(`.product-card[data-product-id="${productId}"]`);
            const images = productCard.querySelectorAll('.product-image');
            let activeIndex = Array.from(images).findIndex(img => img.style.opacity === '1');
            images[activeIndex].style.opacity = '0';
            activeIndex = (activeIndex + direction + images.length) % images.length;
            images[activeIndex].style.opacity = '1';
        }

        function initializeImageSliders() {
            const productCards = document.querySelectorAll('.product-card');
            productCards.forEach(card => {
                let startX;
                let isSwiping = false;
                card.addEventListener('touchstart', e => {
                    startX = e.touches[0].clientX;
                    isSwiping = true;
                });
                card.addEventListener('touchmove', e => {
                    if (!isSwiping) return;
                    const currentX = e.touches[0].clientX;
                    const diff = startX - currentX;
                    if (Math.abs(diff) > 50) {
                        changeImage(card.dataset.productId, diff > 0 ? 1 : -1);
                        isSwiping = false;
                    }
                });
                card.addEventListener('touchend', () => {
                    isSwiping = false;
                });
            });
        }

        function toggleLike(productId) {
            const productRef = database.ref('products/' + productId + '/likes/' + userId);
            productRef.once('value').then((snapshot) => {
                if (snapshot.val()) {
                    productRef.remove();
                } else {
                    productRef.set(true);
                }
            });
        }

        function toggleFavorite(productId) {
            const productRef = database.ref('products/' + productId + '/favorites/' + userId);
            productRef.once('value').then((snapshot) => {
                if (snapshot.val()) {
                    productRef.remove();
                } else {
                    productRef.set(true);
                }
            });
        }

        function toggleSave(productId) {
            const productRef = database.ref('products/' + productId + '/saved/' + userId);
            productRef.once('value').then((snapshot) => {
                if (snapshot.val()) {
                    productRef.remove();
                } else {
                    productRef.set(true);
                }
            });
        }

      async function addProduct() {
    const name = document.getElementById('newProductName').value;
    const imageFiles = document.getElementById('newProductImage').files;
    const priceOriginal = document.getElementById('newProductPriceOriginal').value;
    const priceDiscount = document.getElementById('newProductPriceDiscount').value;
    const priceSuperDiscount = document.getElementById('newProductPriceSuperDiscount').value;
    const fileName = document.getElementById('newProductFileName').value;
    const category = document.getElementById('newProductCategory').value;
    const quantity = document.getElementById('newProductQuantity').value;  // Add quantity field

    if (!name || imageFiles.length === 0 || !priceOriginal || !priceDiscount || !priceSuperDiscount || !fileName || !category || !quantity) {
        alert('الرجاء ملء جميع الحقول');
        return;
    }

    try {
        const imageUrls = await Promise.all(Array.from(imageFiles).map(uploadImage));
        const newProduct = {
            name: name,
            images: imageUrls,
            priceOriginal: priceOriginal,
            priceDiscount: priceDiscount,
            priceSuperDiscount: priceSuperDiscount,
            fileName: fileName,  // Include HTML file name
            category: category,
            quantity: parseInt(quantity)  // Store quantity as a number
        };

        database.ref('products').push(newProduct, function (error) {
            if (error) {
                alert('خطأ في إضافة المنتج: ' + error);
            } else {
                alert('تمت إضافة المنتج بنجاح!');
                toggleAddProductForm();
                filterProductsByCategory(category); // Refresh view after adding the product
            }
        });
    } catch (error) {
        alert('خطأ في رفع الصور: ' + error);
    }
}

function redirectToProductPage(fileName) {
    if (fileName) {
        window.location.href = fileName;
    } else {
        alert('لا يوجد ملف مرتبط بهذا المنتج.');
    }
}



function filterProductsByCategory(category) {
    const productsContainer = document.getElementById('products');
    productsContainer.innerHTML = ''; // مسح المنتجات الحالية

    const selectedCategory = category || document.getElementById('categorySelect').value;

    if (!selectedCategory) {
        productsContainer.innerHTML = '<p>الرجاء اختيار تصنيف لعرض المنتجات.</p>';
        return;
    }

    // جلب المنتجات من قاعدة البيانات بناءً على التصنيف
    database.ref('products').orderByChild('category').equalTo(selectedCategory).once('value', (snapshot) => {
        const products = snapshot.val();

        if (products) {
            for (let key in products) {
                const product = products[key];
                productsContainer.innerHTML += createProductCard(key, product);
            }
        } else {
            productsContainer.innerHTML = '<p>لا توجد منتجات في هذا التصنيف.</p>';
        }

        initializeImageSliders(); // تهيئة السلايدرات إذا كنت تستخدم عرض صور متعدد
    });
}


        async function uploadImage(imageFile) {
            const storageRef = storage.ref('product_images/' + Date.now() + '_' + imageFile.name);
            await storageRef.put(imageFile);
            return await storageRef.getDownloadURL();
        }

        function toggleAddProductForm() {
            const form = document.getElementById('addProductForm');
            form.style.display = form.style.display === 'block' ? 'none' : 'block';
        }

        function toggleSidebar() {
            const sidebar = document.getElementById('mySidebar');
            sidebar.style.left = sidebar.style.left === '0px' ? '-250px' : '0px';
        }

        // دالة جديدة للبحث عن المنتجات
        function searchProducts() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const productsContainer = document.getElementById('products');

            // إذا كان حقل البحث فارغًا، قم بعرض جميع المنتجات
            if (searchTerm === '') {
                fetchProducts();
                return;
            }

            database.ref('products').once('value', (snapshot) => {
                const products = snapshot.val();
                productsContainer.innerHTML = ''; // مسح المنتجات الحالية

                for (let key in products) {
                    const product = products[key];
                    if (product.name.toLowerCase().includes(searchTerm)) {
                        const productCard = createProductCard(key, product);
                        productsContainer.innerHTML += productCard;
                    }
                }

                // إذا لم يتم العثور على منتجات، اعرض رسالة
                if (productsContainer.innerHTML === '') {
                    productsContainer.innerHTML = '<p>لا توجد منتجات مطابقة للبحث.</p>';
                }

                initializeImageSliders();
            });
        }

        // تحديث دالة fetchProducts لتتعامل مع حالة البحث
        function fetchProducts() {
            const productsContainer = document.getElementById('products');
            const searchInput = document.getElementById('searchInput');

            // إذا كان هناك نص في حقل البحث، قم بتنفيذ البحث بدلاً من جلب جميع المنتجات
            if (searchInput.value.trim() !== '') {
                searchProducts();
                return;
            }

            database.ref('products').on('value', (snapshot) => {
                const products = snapshot.val();
                productsContainer.innerHTML = '';
                for (let key in products) {
                    const product = products[key];
                    const productCard = createProductCard(key, product);
                    productsContainer.innerHTML += productCard;
                }
                initializeImageSliders();
                updateCartCount();
            });
        }

        function showPricePopup(productId) {
            currentProductId = productId;
            const popup = document.getElementById('pricePopup');
            const countdown = document.getElementById('countdown');
            const addToCartBtn = document.getElementById('addToCartBtn');
            let timer = 3;
            countdown.innerText = timer;

            const lastPurchaseTime = localStorage.getItem(`lastPurchase_${productId}_${userId}`);
            const currentTime = Date.now();

            if (lastPurchaseTime && currentTime - lastPurchaseTime < 3600000) {
                alert('يمكنك إضافة هذا المنتج مرة واحدة فقط كل ساعة. الرجاء المحاولة لاحقاً.');
                return;
            }

            addToCartBtn.style.display = 'none';
            popup.style.display = 'block';

            const countdownInterval = setInterval(() => {
                timer--;
                countdown.innerText = timer;
                if (timer === 0) {
                    clearInterval(countdownInterval);
                    selectRandomPrice(productId);
                    addToCartBtn.style.display = 'inline-block';
                }
            }, 1000);
        }

        function closePopup() {
            const popup = document.getElementById('pricePopup');
            popup.style.display = 'none';
        }

        function selectRandomPrice(productId) {
            const randomPriceDisplay = document.getElementById('randomPrice');
            database.ref('products/' + productId).once('value', (snapshot) => {
                const product = snapshot.val();
                const prices = [
                    parseFloat(product.priceOriginal),
                    parseFloat(product.priceDiscount),
                    parseFloat(product.priceSuperDiscount)
                ];
                currentPrice = prices[Math.floor(Math.random() * prices.length)];
                randomPriceDisplay.innerText = `السعر الخاص بك: $${currentPrice.toFixed(2)}`;

                localStorage.setItem(`lastPurchase_${productId}_${userId}`, Date.now().toString());
            });
        }

    function addToCart() {
    if (currentProductId && currentPrice) {
        const productRef = database.ref('products/' + currentProductId);

        // Fetch the current product data from Firebase
        productRef.once('value').then((snapshot) => {
            const product = snapshot.val();
            if (product.quantity > 0) {
                const newQuantity = product.quantity - 1;  // Decrease the quantity

                // Update the cart entry in Firebase
                const cartRef = database.ref('carts/' + userId + '/' + currentProductId);
                cartRef.set({
                    name: product.name,
                    images: product.images || [product.image],
                    price: currentPrice,
                    priceOriginal: product.priceOriginal,
                    priceDiscount: product.priceDiscount,
                    priceSuperDiscount: product.priceSuperDiscount,
                    timestamp: Date.now()
                }, (error) => {
                    if (error) {
                        alert('حدث خطأ أثناء إضافة المنتج إلى السلة.');
                    } else {
                        // Update the product quantity in the database
                        productRef.update({ quantity: newQuantity });

                        // Update the product UI (quantity and "Buy" button visibility)
                        const productCard = document.querySelector(`.product-card[data-product-id="${currentProductId}"]`);
                        const stockElement = productCard.querySelector('.stock');
                        const buyButton = productCard.querySelector('.buy-button');
                        
                        // Update stock display in the UI
                        stockElement.textContent = `الكمية المتوفرة: ${newQuantity}`;

                        // Hide the "Buy" button if stock is 0
                        if (newQuantity <= 0) {
                            buyButton.style.display = 'none';
                        }

                        // Close the popup and show a success message
                        alert('تمت إضافة المنتج إلى السلة بنجاح!');
                        closePopup();
                        updateCartCount();
                    }
                });
            } else {
                alert('المنتج غير متوفر.');
            }
        });
    }
}

        function redirectToPurchase(productId) {
            // استرجاع تفاصيل المنتج من قاعدة البيانات
            database.ref('products/' + productId).once('value', (snapshot) => {
                const product = snapshot.val();

                // تخزين تفاصيل المنتج في localStorage
                const productDetails = {
                    name: product.name,
                    images: product.images || [product.image],
                    priceOriginal: product.priceOriginal,
                    priceDiscount: product.priceDiscount,
                    priceSuperDiscount: product.priceSuperDiscount
                };

                localStorage.setItem('selectedProduct', JSON.stringify(productDetails));

                // الانتقال إلى صفحة إتمام الشراء
                window.location.href = "checkout.html";
            });
        }




        function showLikedProducts() {
            const productsContainer = document.getElementById('products');
            productsContainer.innerHTML = '';
            database.ref('products').once('value', (snapshot) => {
                const products = snapshot.val();
                for (let key in products) {
                    const product = products[key];
                    if (product.likes && product.likes[userId]) {
                        const productCard = createProductCard(key, product);
                        productsContainer.innerHTML += productCard;
                    }
                }
                initializeImageSliders();
            });
        }

        function showFavoriteProducts() {
            const productsContainer = document.getElementById('products');
            productsContainer.innerHTML = '';
            database.ref('products').once('value', (snapshot) => {
                const products = snapshot.val();
                for (let key in products) {
                    const product = products[key];
                    if (product.favorites && product.favorites[userId]) {
                        const productCard = createProductCard(key, product);
                        productsContainer.innerHTML += productCard;
                    }
                }
                initializeImageSliders();
            });
        }

        function showSavedProducts() {
            const productsContainer = document.getElementById('products');
            productsContainer.innerHTML = '';
            database.ref('products').once('value', (snapshot) => {
                const products = snapshot.val();
                for (let key in products) {
                    const product = products[key];
                    if (product.saved && product.saved[userId]) {
                        const productCard = createProductCard(key, product);
                        productsContainer.innerHTML += productCard;
                    }
                }
                initializeImageSliders();
            });
        }


        window.onload = () => {
            fetchProducts();
            updateLanguage();
            updateCartCount();
        };



        function toggleSearch() {
            const searchInput = document.getElementById('searchInput');
            searchInput.classList.toggle('active');
            if (searchInput.classList.contains('active')) {
                searchInput.focus();
                // إضافة مستمع حدث للبحث عند كتابة المستخدم
                searchInput.addEventListener('input', searchProducts);
            } else {
                // إزالة مستمع الحدث عند إغلاق البحث
                searchInput.removeEventListener('input', searchProducts);
                // إعادة عرض جميع المنتجات
                fetchProducts();
            }
        }



        function transferCartToCheckout() {
            const cartItems = [];
            database.ref('carts/' + userId).once('value', (snapshot) => {
                const cart = snapshot.val();
                if (cart) {
                    for (let productId in cart) {
                        cartItems.push({
                            productId: productId,
                            ...cart[productId]
                        });
                    }
                    // Store cart items in localStorage
                    localStorage.setItem('cartItems', JSON.stringify(cartItems));
                    // Redirect to checkout page
                    window.location.href = 'checkout.html';
                } else {
                    alert('السلة فارغة');
                }
            });
        }
        // دالة جديدة لتحديث صورة المنتج
        function updateProductImage(selectElement, productId) {
            const selectedImage = selectElement.value;
            const productContainer = selectElement.closest('.order-item');
            const imageElement = productContainer.querySelector('.product-image');
            imageElement.src = selectedImage;

            // تحديث الصورة المختارة في قاعدة البيانات
            database.ref(`carts/${userId}/${productId}/selectedImage`).set(selectedImage);
        }

   // دالة تقوم بفتح الصفحة المطلوبة عند النقر على زر السلة
    function redirectToCartPage() {
        // التأكد من أن البيانات موجودة ومحفوظة في السلة
        transferCartToCheckout(); // نقل بيانات السلة إلى صفحة إتمام الشراء
        
        // هنا يتم تحديد الصفحة الخارجية المراد الانتقال إليها
        window.location.href = 'factorial-script.html'; // استبدل بـ URL الصفحة المطلوبة
    }

    // دالة لنقل بيانات السلة إلى صفحة إتمام الشراء
    function transferCartToCheckout() {
        const cartItems = [];
        database.ref('carts3/' + userId).once('value', (snapshot) => {
            const cart = snapshot.val();
            if (cart) {
                for (let productId in cart) {
                    cartItems.push({
                        productId: productId,
                        ...cart[productId]
                    });
                }
                // تخزين بيانات السلة في localStorage للصفحة الثانية
                localStorage.setItem('cartItems', JSON.stringify(cartItems));
            }
        });
    }

     // Update Clock
        function updateClock() {
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            
            updateFlipCard('hours', hours);
            updateFlipCard('minutes', minutes);
            updateFlipCard('seconds', seconds);
        }
        
           function updateFlipCard(id, newValue) {
            const element = document.getElementById(id);
            if (element.textContent !== newValue) {
                element.classList.add('flip');
                setTimeout(() => {
                    element.textContent = newValue;
                    element.classList.remove('flip');
                }, 150);
            }
        }
        
          
        
        // دالة لتحديث مجموع المشاهدات لكل المستخدمين
function updateTotalViews() {
    // مرجع إلى مجموع المشاهدات في قاعدة البيانات
    const totalViewsRef = database.ref('totalViews');

    // زيادة عدد المشاهدات بمقدار 1 لكل مستخدم يدخل الصفحة
    totalViewsRef.transaction(function (currentTotalViews) {
        return (currentTotalViews || 0) + 1;
    });

    // جلب عدد المشاهدات وتحديث الواجهة
    totalViewsRef.on('value', (snapshot) => {
        const totalViewsCount = snapshot.val() || 0;
        updateFlipCard('views', totalViewsCount); // عرض العدد الكلي للمشاهدات
    });
}

// استدعاء الدالة لتحديث العدد الكلي عند تحميل الصفحة
window.onload = () => {
fetchProducts();
    updateTotalViews(); // تحديث العدد الكلي للمشاهدات
    updateUserViews(); // تحديث عدد مشاهدات المستخدم الفردية
};

  // Function to check if user is new and set up userId in localStorage
            function initializeUserId() {
                let userId = localStorage.getItem('userId');
                if (!userId) {
                    // إذا لم يكن هناك معرف، قم بإنشاء معرف جديد وتخزينه في localStorage
                    userId = 'user_' + Math.random().toString(36).substr(2, 9);
                    localStorage.setItem('userId', userId);
                }
            }

            // Function to increment the subscriber count in the database
            function incrementSubscriberCount() {
                const subscriberCountRef = firebase.database().ref('subscriberCount11');

                // استخدام transaction لزيادة العدد وتجنب مشاكل التزامن
                subscriberCountRef.transaction(function (currentCount) {
                    return (currentCount || 0) + 1;
                }).then(function() {
                    console.log('تم تحديث عدد المشتركين بنجاح!');
                    displaySubscriberCount11(); // عرض العدد المحدث
                }).catch(function(error) {
                    console.error('فشل في تحديث عدد المشتركين:', error);
                });
            }

            // Function to display the subscriber count
            function displaySubscriberCount11() {
                firebase.database().ref('subscriberCount11').on('value', function(snapshot) {
                    const subscriberCount = snapshot.val() || 0;
                    const subscriberCountElement = document.getElementById('subscriberCount11');
                    
                    if (subscriberCountElement) {
                        subscriberCountElement.innerText = subscriberCount;
                    }
                });
            }

            // Function to update the total views for all users
            function updateTotalViews() {
                const totalViewsRef = firebase.database().ref('totalViews');
                totalViewsRef.transaction(currentTotalViews => (currentTotalViews || 0) + 1)
                    .then(() => fetchTotalViews())
                    .catch(error => console.error('Error updating total views:', error));
            }

            function fetchTotalViews() {
                const totalViewsRef = firebase.database().ref('totalViews');
                totalViewsRef.on('value', snapshot => {
                    const totalViewsCount = snapshot.val() || 0;
                    updateFlipCard('views', totalViewsCount);
                });
            }

            // Function to update the clock
            function updateClock() {
                const now = new Date();
                const hours = String(now.getHours()).padStart(2, '0');
                const minutes = String(now.getMinutes()).padStart(2, '0');
                const seconds = String(now.getSeconds()).padStart(2, '0');
                
                updateFlipCard('hours', hours);
                updateFlipCard('minutes', minutes);
                updateFlipCard('seconds', seconds);
            }

            // Function to update the flip card animation
            function updateFlipCard(id, newValue) {
                const element = document.getElementById(id);
                if (element && element.textContent !== newValue) {
                    element.classList.add('flip');
                    setTimeout(() => {
                        element.textContent = newValue;
                        element.classList.remove('flip');
                    }, 150);
                }
            }

            // Call functions on page load
            window.onload = function() {
                initializeUserId(); // إعداد هوية المستخدم إذا لم تكن موجودة
                displaySubscriberCount11(); // عرض عدد المشتركين
                updateTotalViews(); // تحديث عدد المشاهدات الكلي
                updateClock(); // تحديث الساعة
                fetchProducts(); // عرض المنتجات
                updateUserViews(); // تحديث عدد مشاهدات المستخدم الفردية

                // إضافة مستمع لزر الاشتراك لزيادة عدد المشتركين عند النقر
                document.getElementById('subscribeButton').addEventListener('click', function() {
                    incrementSubscriberCount();
                });
            };

            // استدعاء تحديث الساعة كل ثانية
            setInterval(updateClock, 1000);
            
            let currentIndex = 0;
const images = document.querySelectorAll('.carousel img');
const totalImages = images.length;

function showNextImage() {
    images[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % totalImages;
    images[currentIndex].classList.add('active');
}

setInterval(showNextImage, 3000); // تغيير الصورة كل 3 ثواني

        </script>
    </main>
    <!-- ربط ملف الجافا سكريبت -->
    <script src="js/app.js"></script>
</body>
</html>

<script type="text/babel">
  const { useState, useEffect } = React;

  const AdBanner = ({ adImage, targetUrl, isVisible, onClose }) => {
    return (
      isVisible && (
        <div style={{
          position: "fixed",
          top: "45%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          padding: "0",
          transition: "opacity 1.5s, transform 0.5s",
          opacity: isVisible ? 1 : 0,
          zIndex: 1000,
          borderRadius: "20px",
          boxShadow: "0 10px 20px rgba(0, 0, 0, 0.2)",
          width: "100%",
          maxWidth: "300px",
          textAlign: "center",
          backgroundColor: "transparent"
        }}>
          {/* زر إغلاق (X) */}
          <button onClick={onClose} style={{
            position: "absolute",
            top: "15px",
            left: "15px", // تغيير من right إلى left
            background: "rgba(255, 255, 255, 0.8)",
            border: "none",
            borderRadius: "50%",
            padding: "5px",
            cursor: "pointer",
            fontSize: "16px",
            color: "#333",
            zIndex: 1001,
            boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)"
          }}>
            &#10005;
          </button>

          <a href={targetUrl} style={{ textDecoration: "none" }}>
            <img 
              src={adImage} 
              alt="إعلان" 
              style={{ 
                width: "100%", 
                height: "600px", /* تعديل الطول لجعل الصورة طولية */
                objectFit: "cover", 
                borderRadius: "15px", 
                boxShadow: "0 20px 5px rgba(0, 0, 0, 0.2)" 
              }} 
            />
          </a>
        </div>
      )
    );
  };

  const App = () => {
    const [ads, setAds] = useState([]);
    const [currentAdIndex, setCurrentAdIndex] = useState(0);
    const [isVisible, setIsVisible] = useState(true);
    const userId = 'user123';

    useEffect(() => {
      const adsRef = firebase.database().ref('ads');
      adsRef.once('value').then((snapshot) => {
        const data = snapshot.val();
        const adsArray = Object.values(data);
        setAds(adsArray);

        const skippedAds = sessionStorage.getItem(`skippedAds_${userId}`);
        if (skippedAds) {
          const skippedAdsArray = JSON.parse(skippedAds);
          setAds((prevAds) => prevAds.filter((_, index) => !skippedAdsArray.includes(index)));
        }
      });
    }, []);

    const handleClose = () => {
      const skippedAds = sessionStorage.getItem(`skippedAds_${userId}`);
      let skippedAdsArray = skippedAds ? JSON.parse(skippedAds) : [];
      skippedAdsArray.push(currentAdIndex);
      sessionStorage.setItem(`skippedAds_${userId}`, JSON.stringify(skippedAdsArray));

      setIsVisible(false);
      setTimeout(() => {
        const nextAdIndex = currentAdIndex + 1;
        if (nextAdIndex < ads.length) {
          setCurrentAdIndex(nextAdIndex);
          setIsVisible(true);
        } else {
          setIsVisible(false);
        }
      }, 500);
    };

    if (ads.length === 0 || !isVisible) {
      return <div style={{ textAlign: "center", marginTop: "0%" }}>جارٍ تحميل الإعلانات...</div>;
    }

    const currentAd = ads[currentAdIndex];

    return (
      <AdBanner
        adImage={currentAd.adImage}
        targetUrl={currentAd.targetUrl}
        isVisible={isVisible}
        onClose={handleClose}
      />
    );
  };

  ReactDOM.render(<App />, document.getElementById("ad-banner"));
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  @keyframes slideIn {
    from {
      transform: translate(-50%, -70%);
      opacity: 0;
    }
    to {
      transform: translate(-50%, -50%);
      opacity: 1;
    }
  }

  button:hover {
    background-color: rgba(255, 255, 255, 1);
  }
</style>
