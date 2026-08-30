export default function handler(req, res) {
  res.status(200).json({
    ok: true,
    service: "gpp-automaton",
    runtime: "vercel",
    control_auth_configured: Boolean(process.env.GPP_CONTROL_TOKEN),
    google_identity_configured: Boolean(process.env.GOOGLE_SERVICE_ACCOUNT_JSON),
    supabase_admin_configured: Boolean(process.env.SUPABASE_ACCESS_TOKEN),
  });
}
