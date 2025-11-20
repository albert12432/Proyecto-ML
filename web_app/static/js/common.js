// ============================================
// FUNCIONES COMUNES PARA TODAS LAS PÁGINAS
// ============================================

// Animación de entrada para elementos
document.addEventListener('DOMContentLoaded', function() {
    // Agregar clase fade-in a las tarjetas
    const cards = document.querySelectorAll('.card-custom, .hover-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 100);
    });
    
    // Efecto smooth scroll para links internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Función para mostrar mensajes de alerta
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '9999';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);
    
    // Auto-cerrar después de 5 segundos
    setTimeout(() => {
        alertDiv.classList.remove('show');
        setTimeout(() => alertDiv.remove(), 150);
    }, 5000);
}

// Prevenir envíos duplicados de formularios
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Procesando...';
        }
    });
});
