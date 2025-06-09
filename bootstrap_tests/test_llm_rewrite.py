
from llm_adapter import LlmAdapter
import unittest
from unittest.mock import patch


original_text = "Лидерите вдъхновяват своите последователи с личен пример как вършат работата си."
test_chats = {
    "pirate": "Arrr, the captains be inspirin’ their crew by showin’ ‘em how the work’s done with their own hands, savvy",
    "formal": "Лидерите вдъхновяват своите последователи чрез личен пример в изпълнението на професионалните си задължения.",
    "haiku": "Лидери светят,  \nс пример водят смело —  \nследват стъпки техни.",
    "rap fan": "Лидери водят, не само говорят,  \nс личен пример, как си вършат задачата правят.  \nНе празни думи, а действия в игра,  \nте показват пътя, как се стига до една звездa",
    "drug dealer": "Лидерите карат хората си да ги следват, като показват как се върти играта на високо нивo",
    "real estate broker": "Лидерите в недвижимите имоти вдъхновяват своите клиенти и колеги чрез личния си пример и професионализъм във всеки етап от процеса на покупко-продажба"
}


class TestLlmAdapter(unittest.TestCase):
    @patch("llm_adapter.LlmAdapter._llm_call")
    def test_populate_redis_cache(self, mock_chain_invoke):
        for style in test_chats.keys():
            mock_chain_invoke.return_value = test_chats[style]
            initial_response = LlmAdapter(
                prompt=original_text,
                style=style
            ).__repr__()
            self.assertEqual(initial_response, test_chats[style])

    def test_verify_redis_cache_content(self):
        for style in test_chats.keys():
            initial_response = LlmAdapter(
                prompt=original_text,
                style=style
            ).__repr__()
            self.assertEqual(initial_response, test_chats[style])
