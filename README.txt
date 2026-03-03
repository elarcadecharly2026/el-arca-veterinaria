El Arca De Charly — FINAL v3
============================

Incluye:
- Login/Logout + Roles (admin/staff)
- Inventario (CRUD)
- Ventas (con descuento automático de stock al finalizar)
- Auditoría de movimientos (login/logout, inventario y ventas)
- Exportar/Importar CSV de inventario
- Configuración de Marca/Logo (se guarda en DB y logo en static/uploads)
- Administrativo: respaldo de SQLite (descargar vet.db)
- Hardware (Windows): prueba de impresora ESC/POS, apertura de cajón, listado COM, test de escáner

Instalación
-----------
1) (Opcional) Crear y activar venv
   - PowerShell:
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
2) Instalar dependencias base:
     python -m pip install --upgrade pip
     python -m pip install -r requirements.txt
3) (Opcional) En Windows, para Hardware:
     python -m pip install pywin32 wmi pyserial
4) Ejecutar:
     python app.py
5) Abrir:
     http://127.0.0.1:5000

Usuario inicial
---------------
Se crea automáticamente si no existe:
  Usuario: admin@arca.local
  Clave:   admin123
  Rol:     admin

Notas
-----
- La base se guarda en vet.db (junto a app.py).
- Para cambiar ruta de DB, define la variable de entorno DATABASE_URL (ej: sqlite:///C:/Datos/vet.db).
- El logo por defecto está en static/img/arca_logo.png. Puedes subir otro desde "Administrativo → Configuración".
