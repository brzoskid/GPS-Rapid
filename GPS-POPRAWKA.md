RAPID OBD — poprawka GPS

Zachowano oryginalną strukturę projektu i wszystkie pliki z dostarczonego archiwum.
Zmiany:
- www/index.html: jawne sprawdzanie/żądanie uprawnień lokalizacji, obsługa błędów GPS,
  przycisk „WŁĄCZ / PONÓW GPS” i czytelny status zamiast cichego ignorowania błędów.
- tools/patch-manifest.py: idempotentne dodawanie ACCESS_COARSE_LOCATION oraz
  ACCESS_FINE_LOCATION; poprawiono warunek, który wcześniej mógł kończyć skrypt
  przed dodaniem brakujących uprawnień.

Aby uzyskać APK, uruchom workflow GitHub Actions „Build APK” (workflow_dispatch)
lub wypchnij zmiany do repozytorium. To archiwum zawiera projekt źródłowy, nie gotowy APK.
