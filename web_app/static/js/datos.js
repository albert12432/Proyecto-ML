// ============================================
// FUNCIONES PARA INGENIERÍA DE DATOS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Animación para las barras de calidad
    const qualityBars = document.querySelectorAll('.data-quality-bar');
    
    setTimeout(() => {
        qualityBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            bar.style.transition = 'width 1s ease-out';
            
            setTimeout(() => {
                bar.style.width = width;
            }, 100);
        });
    }, 500);
    
    // Animación para los pasos del pipeline
    const pipelineSteps = document.querySelectorAll('.pipeline-step');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateX(-30px)';
                    entry.target.style.transition = 'all 0.6s ease';
                    
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateX(0)';
                    }, 50);
                }, index * 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    pipelineSteps.forEach(step => observer.observe(step));
    
    // Efecto hover mejorado para las tarjetas de fuentes
    const sourceCards = document.querySelectorAll('.card.bg-light');
    sourceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05) translateY(-5px)';
            this.style.transition = 'all 0.3s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) translateY(0)';
        });
    });
});
