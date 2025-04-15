import urllib.parse


class UrlService:
    @staticmethod
    def parse_start_parameters(start_payload: str) -> dict:
        decoded = urllib.parse.unquote(start_payload) if start_payload else ""
        parsed = urllib.parse.parse_qs(decoded)

        return {k: v[0] for k, v in parsed.items()} if parsed else {}

    @staticmethod
    def build_webapp_url(base_url: str, params: dict) -> str:
        if params:
            print(f"{base_url}&{urllib.parse.urlencode(params)}")
            return f"{base_url}&{urllib.parse.urlencode(params)}"
        print(base_url)
        return base_url
