import { useState, useEffect } from "react";
import { setToastCallback } from "@/hooks/useToast";
import { X } from "lucide-react";

export function ToastContainer() {
  const [toasts, setToasts] = useState([]);

  useEffect(() => {
    setToastCallback((message, type) => {
      const id = Date.now();
      const newToast = { id, message, type };
      setToasts((prev) => [...prev, newToast]);

      // Auto remove after 3 seconds
      setTimeout(() => {
        setToasts((prev) => prev.filter((t) => t.id !== id));
      }, 5000);
    });
  }, []);

  const removeToast = (id) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  };

  return (
    <div className="fixed top-[72px] right-6 space-y-2 z-50">
        {toasts.map((toast) => (
        <div
          key={toast.id}
          className={`flex items-center gap-3 rounded-lg px-4 py-3 text-sm font-medium animate-in fade-in slide-in-from-top-2 duration-300 ${
            toast.type === "success"
              ? "bg-green-500/10 text-green-500 border border-green-500/20"
              : toast.type === "error"
                ? "bg-red-500/10 text-red-500 border border-red-500/20"
                : "bg-blue-500/10 text-blue-500 border border-blue-500/20"
          }`}
        >
          {toast.message}
        </div>
      ))}
    </div>
  );
}
