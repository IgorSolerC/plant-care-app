from pathlib import Path
from importlib import import_module

# O diretório base do pacote (app/models)
package_dir = Path(__file__).resolve().parent

# O nome base do módulo para importação (app.models)
base_module_name = __name__

# Usar glob("**/*.py") para encontrar TODOS os arquivos .py recursivamente
for module_file in package_dir.glob("**/*.py"):
    # Ignorar arquivos __init__.py
    if module_file.is_file() and module_file.name != "__init__.py":
        
        # Construir o nome do módulo de forma dinâmica
        # 1. Pega o caminho relativo do arquivo a partir do package_dir
        #    Ex: enums/tipo_luminosidade_enum.py
        relative_path = module_file.relative_to(package_dir)
        
        # 2. Remove a extensão .py e substitui separadores de diretório por pontos
        #    Ex: enums.tipo_luminosidade_enum
        module_path_parts = list(relative_path.with_suffix('').parts)
        
        # 3. Junta tudo para formar o nome completo do módulo
        #    Ex: app.models.enums.tipo_luminosidade_enum
        module_name = f"{base_module_name}.{'.'.join(module_path_parts)}"

        # Importa o módulo dinamicamente para que o SQLAlchemy o registre
        import_module(module_name)