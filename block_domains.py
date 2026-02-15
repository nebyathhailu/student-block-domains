import os

domains_to_block = [
    "openai.com",
    "deepmind.google",
    "www.tabnine.com",
    "www.devseccon.com",
    "wpcode.com",
    "www.askcodi.com",
    "www.codiga.io",
    "visualstudio.microsoft.com",
    "www.aixcoder.com",
    "www.ponicode.com",
    "wingware.com",
    "sourcegraph.com",
    "gemini.google.com",
    "www.anthropic.com",
    "stability.ai",
    "www.blackbox.ai",
    "writesonic.com",
    "bardai.io",
    "socratic.org",
    "chat.openai.com",
    "web.whatsapp.com",
    "www.youtube.com"
    "huggingface.co", "yueai.ai", "gemini.google.com", "speechsynthesis.online", 
    "keychain.com", "datingkiller.com", "runwayml.com", "deepai.org", 
    "playgroundai.com", "dream.ai", "midjourney.com",  "chat.openai.com", "claude.ai", "deepseek.com", "x.ai", "pi.ai", "mistral.ai", "gemini.google.com", "ai.meta.com",
    "perplexity.ai", "you.com", "komo.ai", "neeva.com",
    "stablediffusionweb.com", "midjourney.com", "leonardo.ai", "runwayml.com",
    "synthesia.io", "pika.art", "heygen.com",
    "suno.ai", "udio.com", "elevenlabs.io", "voicify.ai",
    "github.com/features/copilot", "codeium.com", "tabnine.com", "mutable.ai", "aws.amazon.com/codewhisperer",
    "sourcegraph.com/cody", "cursor.sh", "jetbrains.com/ai/", "openai.com/research/codex", "sourcery.ai",
    "notion.so/product/ai", "grammarly.com", "jasper.ai", "copy.ai", "rytr.me",
    "datarobot.com", "monkeylearn.com", "openai.com",
    "deepbrain.io", "replika.com",
    "descript.com", "lumen5.com",
    "hubspot.com", "chatfuel.com", "persado.com",
    "casetext.com", "harvey.ai", "kirasystems.com",
    "ibm.com/watson", "huggingface.co", "cloud.google.com/vertex-ai", "anthropic.com",
    "ai.meta.com/llama", "aws.amazon.com/bedrock", "cohere.com",
    "speechsynthesis.online", "keychain.com", "datingkiller.com","runwayml.com", "deepai.org", "playgroundai.com", "dream.ai", "midjourney.com",
    "tabnine.com", "replit.com", "apify.com", "openai.com/dalle", "murf.ai",
    "codeium.com", "perplexity.ai", "you.com", "phind.com", "leonardo.ai",
    "stablediffusionweb.com", "cohere.ai", "jasper.ai", "openai.com","chat.openai.com",
    "claude.ai",
    "gemini.google.com",
    "pi.ai",
    "mistral.ai",
    "huggingface.co/chat",
    "perplexity.ai",
    "youchat.com",
    "forefront.ai",
    "palm.google.com",
    "openassistant.io",
    "anthropic.com",
    "cohere.com",
    "ai21.com",
    "cloud.google.com/vertex-ai",
    "ibm.com/watson",
    "meta.com/llama",
    "aws.amazon.com/bedrock",
    "deepmind.com",
    "octo.ai",
    "mosaicml.com",
    "quora.com/poe",
    "komo.ai",
    "asksage.ai",
    "coze.com",
    "twin.chat",
    "character.ai",
    "janitorai.com",
    "chatsimple.ai",
    "replika.com",
    "kajiwoto.com",
    "phind.com",
    "andisearch.com",
    "neeva.com",
    "rasa.com",
    "chatbot.com",
    "www.deepseek.com",
    "botpress.com",
    "drift.com",
    "tidio.com",
    "liveperson.com",
    "poly.ai",
    "boost.ai",
    "kore.ai",
    "replicant.ai",
    "https://www.deepseek.com/",
    "chat.deepseek.com",
    "https://chat.deepseek.com/",
    "deepseek.com"
]

hosts_path = "/etc/hosts"
redirect_ip = "127.0.0.1"

# Read existing entries from /etc/hosts 
existing_domains = set()
with open(hosts_path, "r") as hosts_file:
    for line in hosts_file:
        parts = line.split()
        if len(parts) >= 2 and parts[0] in ["127.0.0.1", "0.0.0.0"]:
            existing_domains.add(parts[1])

# Append only new domains
with open(hosts_path, "a") as hosts_file:
    for domain in domains_to_block:
        if domain not in existing_domains:
            hosts_file.write(f"{redirect_ip} {domain}\n")

print("Blocking complete. Flush the DNS cache for changes to take effect.")