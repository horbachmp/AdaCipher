import json
import os
from datetime import datetime
from uuid import uuid4
from pathlib import Path
from typing import Any, Dict, Optional, List, Tuple


class ModelLogger:
    """Logger for logging all model requests and responses"""

    def __init__(self, model_name: str, **config_params):
        """
        Initializes the logger for the model

        Args:
            model_name: Model name
            **config_params: All model configuration parameters (temperature, seed, etc.)
        """
        self.model_run_id = str(uuid4())
        self.model_name = model_name
        self.config_params = config_params

        # Create the log directory
        self.log_dir = Path("system_logs") / "models" / "api" / self.model_run_id
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Save the model config
        self._save_config()

    def _save_config(self):
        """Saves the model config to a JSON file"""
        config = {
            "model_run_id": self.model_run_id,
            "model_name": self.model_name,
            "created_at": datetime.now().isoformat(),
            "parameters": self.config_params
        }

        config_path = self.log_dir / "config.json"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    def log_request(self,
                   question: str,
                   system_prompt: Optional[str] = None,
                   few_shot: Optional[List] = None,
                   **extra_params):
        """
        Logs a request to the model

        Args:
            question: User question/prompt
            system_prompt: System prompt
            few_shot: Few-shot examples
            **extra_params: Additional request parameters
        """
        request_log = {
            "timestamp": datetime.now().isoformat(),
            "type": "request",
            "question": question,
            "system_prompt": system_prompt,
            "few_shot": few_shot,
            "extra_params": extra_params
        }

        self._append_to_log("requests.jsonl", request_log)

    def log_response(self,
                    response: str,
                    success: bool = True,
                    error: Optional[str] = None,
                    **extra_params):
        """
        Logs a model response

        Args:
            response: Model response
            success: Whether the request succeeded
            error: Error text if there was one
            **extra_params: Additional response parameters
        """
        response_log = {
            "timestamp": datetime.now().isoformat(),
            "type": "response",
            "response": response,
            "success": success,
            "error": error,
            "extra_params": extra_params
        }

        self._append_to_log("responses.jsonl", response_log)

    def _append_to_log(self, filename: str, log_entry: Dict[str, Any]):
        """Appends an entry to the JSONL file"""
        log_path = self.log_dir / filename

        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
