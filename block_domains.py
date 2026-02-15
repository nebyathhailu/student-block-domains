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

127.0.0.1 openai.com
127.0.0.1 chat.openai.com
127.0.0.1 openai.com.research
127.0.0.1 openassistant.io

127.0.0.1 deepseek.com
127.0.0.1 www.deepseek.com
127.0.0.1 chat.deepseek.com

127.0.0.1 anthropic.com
127.0.0.1 claude.ai

127.0.0.1 gemini.google.com
127.0.0.1 deepmind.google
127.0.0.1 palm.google.com

127.0.0.1 mistral.ai
127.0.0.1 pi.ai
127.0.0.1 cohere.com
127.0.0.1 cohere.ai
127.0.0.1 ai21.com
127.0.0.1 octo.ai
127.0.0.1 mosaicml.com

127.0.0.1 huggingface.co
127.0.0.1 stability.ai
127.0.0.1 stablediffusionweb.com
127.0.0.1 leonardo.ai
127.0.0.1 runwayml.com
127.0.0.1 deepai.org
127.0.0.1 playgroundai.com
127.0.0.1 dream.ai
127.0.0.1 midjourney.com

127.0.0.1 elevenlabs.io
127.0.0.1 murf.ai
127.0.0.1 suno.ai
127.0.0.1 udio.com
127.0.0.1 voicify.ai
127.0.0.1 speechsynthesis.online

127.0.0.1 synthesia.io
127.0.0.1 pika.art
127.0.0.1 heygen.com
127.0.0.1 deepbrain.io

127.0.0.1 character.ai
127.0.0.1 replika.com
127.0.0.1 janitorai.com
127.0.0.1 kajiwoto.com
127.0.0.1 chatsimple.ai
127.0.0.1 twin.chat
127.0.0.1 forefront.ai

127.0.0.1 perplexity.ai
127.0.0.1 you.com
127.0.0.1 youchat.com
127.0.0.1 phind.com
127.0.0.1 andisearch.com
127.0.0.1 neeva.com
127.0.0.1 komo.ai
127.0.0.1 asksage.ai
127.0.0.1 coze.com

127.0.0.1 botpress.com
127.0.0.1 drift.com
127.0.0.1 tidio.com
127.0.0.1 liveperson.com
127.0.0.1 poly.ai
127.0.0.1 boost.ai
127.0.0.1 kore.ai
127.0.0.1 replicant.ai
127.0.0.1 chatbot.com
127.0.0.1 rasa.com

127.0.0.1 github.com
127.0.0.1 replit.com
127.0.0.1 apify.com

127.0.0.1 tabnine.com
127.0.0.1 codeium.com
127.0.0.1 mutable.ai
127.0.0.1 sourcery.ai
127.0.0.1 cursor.sh

127.0.0.1 jetbrains.com
127.0.0.1 aws.amazon.com
127.0.0.1 cloud.google.com
127.0.0.1 ibm.com
127.0.0.1 meta.com

127.0.0.1 notion.so
127.0.0.1 grammarly.com
127.0.0.1 jasper.ai
127.0.0.1 copy.ai
127.0.0.1 rytr.me
127.0.0.1 writesonic.com

127.0.0.1 datarobot.com
127.0.0.1 monkeylearn.com

127.0.0.1 casetext.com
127.0.0.1 harvey.ai
127.0.0.1 kirasystems.com

127.0.0.1 descript.com
127.0.0.1 lumen5.com

127.0.0.1 hubspot.com
127.0.0.1 chatfuel.com
127.0.0.1 persado.com

127.0.0.1 keychain.com
127.0.0.1 datingkiller.com

127.0.0.1 web.whatsapp.com
127.0.0.1 youtube.com
127.0.0.1 www.youtube.com
127.0.0.1 socratic.org
127.0.0.1 wpcode.com
127.0.0.1 devseccon.com
127.0.0.1 wingware.com
127.0.0.1 sourcegraph.com
127.0.0.1 blackbox.ai
127.0.0.1 askcodi.com
127.0.0.1 codiga.io
127.0.0.1 aixcoder.com
127.0.0.1 ponicode.com
127.0.0.1 x.ai
127.0.0.1 quora.com