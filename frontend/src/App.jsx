import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [conversations, setConversations] = useState([]);
  const [conversationId, setConversationId] = useState(null);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const [view, setView] = useState("chat");
  useEffect(() => {
    loadConversations();
  }, []);

  useEffect(() => {
    loadCurrentUser();
  }, []);

const filteredConversations = conversations.filter((conv) =>
  conv.title.toLowerCase().includes(searchTerm.toLowerCase())
);

async function loadCurrentUser() {
  const token = localStorage.getItem("token");

  if (!token) return;

  const res = await fetch("http://127.0.0.1:8000/auth/me", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    localStorage.removeItem("token");
    return;
  }

  const data = await res.json();
  setUser(data);
}

async function login() {
  const res = await fetch("http://127.0.0.1:8000/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  const data = await res.json();

  if (!res.ok) {
    alert(data.detail || "Login failed");
    return;
  }

  localStorage.setItem("token", data.access_token);

  await loadCurrentUser();
  await loadConversations();
}

function logout() {
  localStorage.removeItem("token");
  setUser(null);
  setMessages([]);
  setConversationId(null);
  setConversations([]);
}

async function loadConversations() {
  const token = localStorage.getItem("token");

  if (!token) {
    setConversations([]);
    return;
  }

  const res = await fetch("http://127.0.0.1:8000/conversations", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    setConversations([]);
    return;
  }

  const data = await res.json();
  setConversations(data);
}

  async function openConversation(id) {
  const token = localStorage.getItem("token");

  setConversationId(id);

  const res = await fetch(
    `http://127.0.0.1:8000/conversations/${id}/messages`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!res.ok) return;

  const data = await res.json();

  setMessages(
    data.map((msg) => ({
      role: msg.role,
      content: msg.content,
    }))
  );
}

  function startNewChat() {
    setConversationId(null);
    setMessages([]);
    setInput("");
  }

async function deleteConversation(id, e) {
  e.stopPropagation();

  const token = localStorage.getItem("token");

  const res = await fetch(`http://127.0.0.1:8000/conversations/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    console.error("Delete failed:", await res.text());
    return;
  }

  if (conversationId === id) {
    startNewChat();
  }

  loadConversations();
}

async function uploadFile(file, convId) {
  const token = localStorage.getItem("token");

  const formData = new FormData();
  formData.append("file", file);

  let url = "http://127.0.0.1:8000/files/upload";

  if (convId) {
    url += `?conversation_id=${convId}`;
  }

  const res = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
    },
    body: formData,
  });

  if (!res.ok) {
    alert("File upload failed");
    return null;
  }

  return await res.json();
}

async function sendMessage() {
  if (!input.trim() && !selectedFile) return;

  const token = localStorage.getItem("token");

  if (!token || token === "undefined") {
    alert("Please login again. Token is missing.");
    return;
  }

  let activeConversationId = conversationId;
  let uploadedFile = null;

  if (selectedFile) {
    uploadedFile = await uploadFile(selectedFile, activeConversationId);

    if (!uploadedFile) return;

    activeConversationId = uploadedFile.conversation_id;
    setConversationId(activeConversationId);
    setSelectedFile(null);
  }

  const currentInput = input.trim() || "Summarize the uploaded document";

  const payload = {
    message: currentInput,
  };

  if (activeConversationId) {
    payload.conversation_id = activeConversationId;
  }

  setMessages((prev) => [
    ...prev,
    { role: "user", content: currentInput },
    { role: "assistant", content: "" },
  ]);

  setInput("");

  const response = await fetch("http://127.0.0.1:8000/chat/stream", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(payload),
  });

  console.log(response);

  if (!response.ok) {
    const error = await response.json();

    setMessages((prev) => {
      const updated = [...prev];
      updated[updated.length - 1] = {
        role: "assistant",
        content: `Error: ${error.detail}`,
      };
      return updated;
    });

    return;
  }

  const newConversationId = response.headers.get("X-Conversation-Id");

  if (newConversationId) {
    setConversationId(newConversationId);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);

    setMessages((prev) => {
      const updated = [...prev];
      const lastIndex = updated.length - 1;

      updated[lastIndex] = {
        ...updated[lastIndex],
        content: updated[lastIndex].content + chunk,
      };

      return updated;
    });
  }

  loadConversations();
}


  if (!localStorage.getItem("token")) {
  return (
    <div className="login-page">
      <div className="login-card">
        <div className="login-logo">AI</div>

        <h1>Welcome Back</h1>
        <p>Login to continue your AI conversations</p>

        <input
          className="login-input"
          placeholder="Email address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="login-input"
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="login-button" onClick={login}>
          Login
        </button>
      </div>
    </div>
  );
}

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="logo">💬</div>
          <h2>Simple ChatGPT</h2>
        </div>

        <button className="new-chat" onClick={startNewChat}>
          + New Chat
        </button>

        <input
          className="search-input"
          placeholder="Search conversations..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        <div className="section-title">Conversations</div>

        <div className="conversation-list">
          {filteredConversations.map((conv) => (
              <div
              key={conv.id}
              className={`conversation-item ${
                conversationId === conv.id ? "active" : ""
              }`}
              onClick={() => openConversation(conv.id)}
            >
              <span>{conv.title}</span>

              <button
                className="delete-btn"
                onClick={(e) => deleteConversation(conv.id, e)}
              >
                🗑
              </button>
            </div>
          ))}
        </div>

        <div className="user-section">
          
            <div className="user-header">
              <div className="user-avatar">
                {user?.name?.charAt(0).toUpperCase()}
              </div>

              <div className="user-info">
                <div className="user-name">
                  {user?.name}
                </div>

                <div className="user-email">
                  {user?.email}
                </div>
              </div>

              
            </div>

            <button
              className="modern-logout-btn"
              onClick={logout}
            >
              <span className="logout-icon">↪</span>
              Logout
            </button>
          </div>
        
      </aside>

      <main className="main">
        <header className="topbar">
          <h1>Simple ChatGPT App</h1>

          <div className="top-actions">
            <button>Share</button>
            <div className="user-avatar">{user?.name?.charAt(0).toUpperCase()}</div>
          </div>
        </header>

        <section className="chat-area">
          {messages.length === 0 && (
            <div className="empty-state">
              <h2>How can I help you today?</h2>
              <p>Ask anything and start a new conversation.</p>
            </div>
          )}

          {messages.map((msg, index) => (
            <div key={index} className={`message-card ${msg.role}`}>
              <div className="message-icon">
                {msg.role === "user" ? "👤" : "🤖"}
              </div>

              <div className="message-content">
                <div className="message-header">
                  <strong>{msg.role === "user" ? "You" : "AI"}</strong>
                </div>

                <p>{msg.content}</p>
              </div>
            </div>
          ))}
        </section>

        <footer className="input-wrapper">
          <div className="composer-wrapper">
            {selectedFile && (
              <div className="attached-file">
                📎 {selectedFile.name}
                <button onClick={() => setSelectedFile(null)}>×</button>
              </div>
            )}

            <div className="composer">
              <label className="file-upload-btn">
                📎
                <input
                  type="file"
                  hidden
                  onChange={(e) => setSelectedFile(e.target.files[0])}
                />
              </label>

              <input
                className="chat-input"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask anything..."
                onKeyDown={(e) => {
                  if (e.key === "Enter") sendMessage();
                }}
              />

              <button className="send-btn" onClick={sendMessage}>
                ➤
              </button>
            </div>

            <p className="disclaimer">
              AI can make mistakes. Consider checking important information.
            </p>
          </div>
        </footer>
      </main>
    </div>
  );
}

export default App;