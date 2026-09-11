import importlib.util
from pathlib import Path


def load_module_from_file(py_path: str):
        py_path = str(Path(py_path))
        module_name = Path(py_path).stem

        spec = importlib.util.spec_from_file_location(module_name, py_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        custom_class = None
        for attr_name in dir(module):
            if not attr_name.startswith('_'):
                attr = getattr(module, attr_name)
                if isinstance(attr, type):
                    custom_class = attr
                    break

        if custom_class is None:
            raise ValueError(f"No custom class found in module: {py_path}")
        return custom_class
