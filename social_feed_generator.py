import csv
import json
import os
import random
from datetime import datetime, timedelta

try:
    # SDK moderno de OpenAI (>= 1.0)
    from openai import OpenAI
except ImportError:
    OpenAI = None


"""
Script: social_feed_generator.py

Propósito:
- Leer perfiles/prospectos desde un CSV (exportado de PhantomBuster, Apify, etc.).
- Opcionalmente, generar mensajes personalizados con OpenAI (según tu prompt).
- Agregar métricas agregadas (leads, citas, mercados, respuestas).
- Escribir un archivo JSON (`social_feed.json`) que tu landing lee para:
    - Actualizar el dashboard de métricas.
    - Mostrar eventos recientes tipo "Live Social Proof".

Cómo usarlo (flujo simple recomendado):
1. Exporta tus prospectos a `prospects.csv` en este mismo directorio
   con columnas como:
      nombre, cargo, empresa, bio, red, mercado
2. Configura tu API key de OpenAI:
      setx OPENAI_API_KEY "tu_clave_aqui"   (en Windows)
3. (Opcional) Ajusta PROMPT_BASE y MAX_PROSPECTS para controlar coste.
4. Ejecuta:
      python social_feed_generator.py
5. Sirve tu landing (por ejemplo):
      python -m http.server 8000
   y abre:
      http://localhost:8000/
   La página intentará leer `social_feed.json` y actualizar el dashboard.

IMPORTANTE:
- Respeta siempre los Términos de Servicio de cada red social.
- Idealmente usa herramientas oficiales (APIs) o servicios especializados
  (PhantomBuster, Apify, etc.) para recolectar datos y solo luego pásalos a este script.
"""


INPUT_CSV = os.environ.get("MAO_PROSPECTS_CSV", "prospects.csv")
OUTPUT_JSON = os.environ.get("MAO_SOCIAL_FEED_JSON", "social_feed.json")
OPENAI_MODEL = os.environ.get("MAO_OPENAI_MODEL", "gpt-4.1-mini")
MAX_PROSPECTS = int(os.environ.get("MAO_MAX_PROSPECTS", "30"))


PROMPT_BASE = """Actúa como experto en ventas B2B.
Tengo un prospecto llamado {nombre} que trabaja en {empresa} como {cargo}.
Esta es su bio o contexto: {bio}

Escribe un mensaje corto (máximo 250 caracteres) para Instagram/LinkedIn.
NO suenes robótico.
NO digas "Espero que estés bien".
Objetivo: ofrecerle una automatización con IA para ahorrarle tiempo.
Menciona un dolor común de su cargo.
Termina con una pregunta cerrada."""


def load_prospects(path: str):
    if not os.path.exists(path):
        print(f"[WARN] No se encontró el CSV de prospectos en: {path}")
        print("       Crea un archivo 'prospects.csv' o define MAO_PROSPECTS_CSV.")
        return []

    prospects = []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prospects.append(row)
    return prospects[:MAX_PROSPECTS]


def get_openai_client():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("[INFO] OPENAI_API_KEY no definida. Se generarán mensajes básicos sin IA.")
        return None
    if OpenAI is None:
        print("[WARN] Paquete 'openai' no instalado. Ejecuta: pip install openai")
        return None
    return OpenAI(api_key=api_key)


def generate_message_with_ai(client, prospect: dict) -> str:
    nombre = prospect.get("nombre") or "este prospecto"
    empresa = prospect.get("empresa") or "tu empresa"
    cargo = prospect.get("cargo") or "tu rol"
    bio = prospect.get("bio") or "Sin bio disponible."

    prompt = PROMPT_BASE.format(nombre=nombre, empresa=empresa, cargo=cargo, bio=bio)

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "Eres un copywriter experto en prospección B2B con IA."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=150,
        )
        text = response.choices[0].message.content.strip()
        # Nos aseguramos de que no sea larguísimo
        return text[:260]
    except Exception as e:
        print(f"[ERROR] Falló OpenAI para {nombre}: {e}")
        # Fallback genérico
        return (
            f"Hola {nombre}, veo lo que haces en {empresa}. "
            "Tengo un sistema de IA que automatiza tu prospección y respuestas. "
            "¿Quieres que te muestre cómo en 15 min?"
        )


def build_summary_and_events(prospects, use_ai: bool):
    now = datetime.utcnow()

    # Métricas muy sencillas (puedes cambiarlas por algo real)
    leads_qualified = len(prospects)
    meetings_booked = max(1, leads_qualified // 10) if leads_qualified else 0
    auto_responses = leads_qualified * 3
    markets_tracked = len({p.get("mercado") for p in prospects if p.get("mercado")}) or 1

    summary = {
        "leads_qualified": leads_qualified,
        "meetings_booked": meetings_booked,
        "auto_responses": auto_responses,
        "markets_tracked": markets_tracked,
        "leads_growth": random.choice([15, 28, 40, 55]),  # Simulación
        "meetings_growth": random.choice([12, 25, 32]),   # Simulación
    }

    # Eventos tipo "Live Social Proof"
    base_messages = [
        "Agente Mao acaba de generar {n} leads para una inmobiliaria en Bogotá.",
        "Scraping completado: {n} prospectos encontrados para un e‑commerce.",
        "Nueva campaña lanzada: agentes prospectando CEOs de startups en LinkedIn.",
        "Reporte actualizado: seguimiento de precios para {n} competidores en sector legal.",
        "Asistente IA agendó {m} citas en Calendly para una agencia de marketing.",
    ]

    events = []
    for i in range(min(5, max(1, leads_qualified))):
        delta_minutes = random.randint(1, 60)
        ts = now - timedelta(minutes=delta_minutes)
        msg_template = random.choice(base_messages)
        message = msg_template.format(
            n=max(5, leads_qualified + random.randint(0, 20)),
            m=max(1, meetings_booked + random.randint(0, 3)),
        )
        events.append(
            {
                "message": message,
                "time": ts.isoformat() + "Z",
                "time_ago": f"hace {delta_minutes} min",
            }
        )

    # Si hay prospectos, añadimos alguno con nombre real
    for p in prospects[:3]:
        nombre = p.get("nombre") or "un prospecto"
        empresa = p.get("empresa") or "una empresa"
        events.append(
            {
                "message": f"Se generó un mensaje personalizado para {nombre} de {empresa} listo para enviar.",
                "time": now.isoformat() + "Z",
                "time_ago": "hace segundos",
            }
        )

    return summary, events


def main():
    prospects = load_prospects(INPUT_CSV)
    client = get_openai_client()
    use_ai = client is not None

    print(f"[INFO] Prospectos cargados: {len(prospects)}")
    print(f"[INFO] IA activa: {'sí' if use_ai else 'no'}")

    enriched = []
    for p in prospects:
        mensaje = None
        if use_ai:
            mensaje = generate_message_with_ai(client, p)
        else:
            # Mensaje básico si no hay IA disponible
            nombre = p.get("nombre") or "allí"
            empresa = p.get("empresa") or "tu empresa"
            mensaje = (
                f"Hola {nombre}, vi lo que haces en {empresa}. "
                "Tengo un sistema de IA que automatiza prospección y seguimiento. "
                "¿Te muestro cómo en 15 min?"
            )

        enriched.append(
            {
                "nombre": p.get("nombre"),
                "cargo": p.get("cargo"),
                "empresa": p.get("empresa"),
                "bio": p.get("bio"),
                "red": p.get("red"),
                "mercado": p.get("mercado"),
                "mensaje_personalizado": mensaje,
            }
        )

    summary, events = build_summary_and_events(enriched, use_ai=use_ai)

    payload = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "summary": summary,
        "events": events,
        "prospects": enriched,
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"[OK] Datos escritos en {OUTPUT_JSON}")
    print("     Tu landing ahora puede leer este archivo para mostrar el dashboard y el Live Social Proof.")


if __name__ == "__main__":
    main()

