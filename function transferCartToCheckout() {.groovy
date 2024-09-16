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
                <button id="checkoutButton" class="buy-button" onclick="transferCartToCheckout()">
                    الانتقال إلى صفحة إتمام الشراء
                </button>
            `;
        } else {
            productsContainer.innerHTML += '<p>السلة فارغة</p>';
        }
    });
}




// تحديث دالة addToCart
function addToCart() {
    if (currentProductId && currentPrice) {
        database.ref('products/' + currentProductId).once('value', (snapshot) => {
            const product = snapshot.val();
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
                    alert('تمت إضافة المنتج إلى السلة بنجاح!');
                    closePopup();
                    updateCartCount();
                }
            });
        });
    }
}

// تحديث دالة createCartItemCard
function createCartItemCard(productId, product) {
    return `
        <div class="product-card" data-product-id="${productId}">
            <div class="product-images">
                <img src="${product.images[0]}" alt="${product.name}" class="product-image" style="width: 250px; height: 250px;">
            </div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p class="price">السعر المختار: $${product.price.toFixed(2)}</p>
                <p class="price">السعر الأصلي: $${product.priceOriginal}</p>
                <p class="price">سعر الخصم: $${product.priceDiscount}</p>
                <p class="price">سعر الخصم الفائق: $${product.priceSuperDiscount}</p>
                <button class="action-button" onclick="removeFromCart('${productId}')">
                    <i class="fas fa-trash"></i> إزالة من السلة
                </button>
            </div>
        </div>
    `;
}

// تحديث دالة showCart
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