const API_BASE_URL = 'http://localhost:5000/api';

document.addEventListener('DOMContentLoaded', () => {
    loadServices();
    loadCart();
});

// Format currency
const formatCurrency = (amount) => {
    return new Intl.NumberFormat('es-AR', {
        style: 'currency',
        currency: 'ARS',
        minimumFractionDigits: 0
    }).format(amount);
};

// Fetch and display services
async function loadServices() {
    const servicesList = document.getElementById('services-list');
    try {
        const response = await fetch(`${API_BASE_URL}/services`);
        if (!response.ok) throw new Error('Network response was not ok');
        const services = await response.json();
        
        servicesList.innerHTML = '';
        services.forEach(service => {
            const card = document.createElement('div');
            card.className = 'service-card';
            card.innerHTML = `
                <div>
                    <div class="service-name">${service.servicio}</div>
                    <div class="service-price">${formatCurrency(service.precio)}</div>
                </div>
                <button class="add-btn" onclick="addToCart(${service.id})">
                    Agregar al Carrito
                </button>
            `;
            servicesList.appendChild(card);
        });
    } catch (error) {
        console.error('Error fetching services:', error);
        servicesList.innerHTML = `<div class="empty-cart-msg" style="color: #ef4444;">Error al cargar los servicios. Asegúrese de que el servidor esté ejecutándose.</div>`;
    }
}

// Fetch and display cart
async function loadCart() {
    const cartContainer = document.getElementById('cart-items');
    const cartTotalAmount = document.getElementById('cart-total');
    const checkoutBtn = document.getElementById('checkout-btn');
    
    try {
        const response = await fetch(`${API_BASE_URL}/cart`);
        if (!response.ok) throw new Error('Network response was not ok');
        const cartData = await response.json();
        
        cartContainer.innerHTML = '';
        
        if (cartData.items.length === 0) {
            cartContainer.innerHTML = '<div class="empty-cart-msg">Tu carrito está vacío</div>';
            checkoutBtn.disabled = true;
        } else {
            cartData.items.forEach(item => {
                const cartItem = document.createElement('div');
                cartItem.className = 'cart-item';
                cartItem.innerHTML = `
                    <div class="cart-item-header">
                        <span class="cart-item-name">${item.servicio}</span>
                        <button class="remove-btn" onclick="removeFromCart(${item.item_id})" title="Eliminar">&times;</button>
                    </div>
                    <div class="cart-item-details">
                        <span>Cant: ${item.cantidad} x ${formatCurrency(item.precio_unitario)}</span>
                        <span class="cart-item-subtotal">${formatCurrency(item.subtotal)}</span>
                    </div>
                `;
                cartContainer.appendChild(cartItem);
            });
            checkoutBtn.disabled = false;
        }
        
        cartTotalAmount.textContent = formatCurrency(cartData.total);
    } catch (error) {
        console.error('Error fetching cart:', error);
    }
}

// Add item to cart
async function addToCart(serviceId) {
    try {
        const response = await fetch(`${API_BASE_URL}/cart`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                service_id: serviceId,
                cantidad: 1 // Default to 1 for simplicity
            })
        });
        
        if (response.ok) {
            // Trigger a small visual feedback here if desired
            loadCart();
        } else {
            const err = await response.json();
            alert(`Error: ${err.error}`);
        }
    } catch (error) {
        console.error('Error adding to cart:', error);
    }
}

// Remove item from cart
async function removeFromCart(itemId) {
    try {
        const response = await fetch(`${API_BASE_URL}/cart/${itemId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            loadCart();
        } else {
            const err = await response.json();
            alert(`Error: ${err.error}`);
        }
    } catch (error) {
        console.error('Error removing from cart:', error);
    }
}
