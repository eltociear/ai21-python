from typing import Optional, List

from ai21.clients.common.completion_base import Completion
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import Penalty, CompletionsResponse


class StudioCompletion(StudioResource, Completion):
    def create(
        self,
        model: str,
        prompt: str,
        *,
        max_tokens: int = 64,
        num_results: int = 1,
        min_tokens: int = 0,
        temperature: float = 0.7,
        top_p: float = 1,
        top_k_return: int = 0,
        custom_model: Optional[str] = None,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
        **kwargs,
    ) -> CompletionsResponse:
        url = f"{self._client.get_base_url()}/{model}"

        if custom_model is not None:
            url = f"{url}/{custom_model}"

        url = f"{url}/{self._module_name}"
        body = self._create_body(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            num_results=num_results,
            min_tokens=min_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k_return=top_k_return,
            custom_model=custom_model,
            stop_sequences=stop_sequences,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            count_penalty=count_penalty,
        )
        return self._json_to_response(self._post(url=url, body=body))
