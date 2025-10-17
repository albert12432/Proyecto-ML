// ============================================
// FUNCIONES PARA MODELO NEURAL
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.querySelector('.upload-area');
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/jpeg,image/png';
    fileInput.style.display = 'none';
    document.body.appendChild(fileInput);
    
    const analyzeBtn = document.querySelector('.btn-success');
    const commandOutput = document.querySelector('.command-output');
    const preview = document.getElementById('preview');
    
    // Click en el área de carga
    if (uploadArea) {
        uploadArea.addEventListener('click', () => fileInput.click());
        
        // Drag and Drop
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.style.borderColor = '#f093fb';
            uploadArea.style.backgroundColor = '#fff5fb';
        });
        
        uploadArea.addEventListener('dragleave', () => {
            uploadArea.style.borderColor = '#dee2e6';
            uploadArea.style.backgroundColor = '#fff';
        });
        
        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.style.borderColor = '#dee2e6';
            uploadArea.style.backgroundColor = '#fff';
            
            const file = e.dataTransfer.files[0];
            if (file && file.type.startsWith('image/')) {
                handleImageUpload(file);
            }
        });
    }
    
    // Cambio de archivo
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            handleImageUpload(file);
        }
    });
    
    // Función para manejar la carga de imagen
    function handleImageUpload(file) {
        const reader = new FileReader();
        
        reader.onload = (e) => {
            preview.src = e.target.result;
            preview.classList.remove('d-none');
            analyzeBtn.disabled = false;
            
            // Actualizar output
            commandOutput.innerHTML = `
                <div class="mb-2">
                    <span class="text-info">$</span> Imagen cargada: ${file.name}
                </div>
                <div class="mt-3">
                    <span class="text-muted">// Haz clic en "Analizar Imagen" para procesar</span>
                </div>
            `;
        };
        
        reader.readAsDataURL(file);
    }
    
    // Botón de análisis
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', function() {
            if (!preview.src || preview.classList.contains('d-none')) {
                showAlert('Por favor, carga una imagen primero', 'warning');
                return;
            }
            
            // Simular análisis
            this.disabled = true;
            this.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Analizando...';
            
            commandOutput.innerHTML = `
                <div class="mb-2">
                    <span class="text-info">$</span> Procesando imagen...
                </div>
                <div class="mt-2">
                    <span class="text-warning">⚡ Analizando con CNN...</span>
                </div>
            `;
            
            // Simular procesamiento (2-3 segundos)
            setTimeout(() => {
                const comandos = ['MOVE_UP', 'MOVE_DOWN', 'ROTATE', 'ZOOM_IN', 'SAVE', 'START'];
                const comandoAleatorio = comandos[Math.floor(Math.random() * comandos.length)];
                const confianza = (85 + Math.random() * 10).toFixed(1);
                
                commandOutput.innerHTML = `
                    <div class="mb-2">
                        <span class="text-info">$</span> Análisis completado ✓
                    </div>
                    <div class="mt-2">
                        <span class="text-success">✓ Comando detectado: <strong>${comandoAleatorio}</strong></span>
                    </div>
                    <div class="mt-2">
                        <span class="text-info">ℹ Confianza: ${confianza}%</span>
                    </div>
                    <div class="mt-3">
                        <span class="text-muted">// Procesado en 2.3 segundos</span>
                    </div>
                `;
                
                analyzeBtn.disabled = false;
                analyzeBtn.innerHTML = '<i class="fas fa-play me-2"></i>Analizar Imagen';
                
                showAlert(`¡Comando ${comandoAleatorio} detectado con ${confianza}% de confianza!`, 'success');
            }, 2300);
        });
    }
    
    // Animación para las capas de la red neural
    const neuralLayers = document.querySelectorAll('.neural-layer');
    neuralLayers.forEach((layer, index) => {
        setTimeout(() => {
            layer.style.opacity = '0';
            layer.style.transform = 'translateX(-20px)';
            layer.style.transition = 'all 0.5s ease';
            
            setTimeout(() => {
                layer.style.opacity = '1';
                layer.style.transform = 'translateX(0)';
            }, 50);
        }, index * 100);
    });
});
