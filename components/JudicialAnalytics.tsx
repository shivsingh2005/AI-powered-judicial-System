import React, { useEffect, useState } from 'react';
import { getJudicialAnalytics } from '../services/geminiService';
import { useTranslations } from '../hooks/useTranslations';

export const JudicialAnalytics: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<any>(null);
  const t = useTranslations();

  useEffect(() => {
    let mounted = true;
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const resp = await getJudicialAnalytics('General national caseload overview', 'last_5_years');
        if (!mounted) return;
        setData(resp);
      } catch (err: any) {
        setError(err.message || String(err));
      } finally {
        setLoading(false);
      }
    };
    fetchData();
    return () => { mounted = false; };
  }, []);

  if (loading) return <div className="p-4 bg-[rgb(var(--card))] rounded">Loading judicial analytics…</div>;
  if (error) return <div className="p-4 bg-red-50 text-red-700 rounded">Error: {error}</div>;
  if (!data) return null;

  return (
    <div className="bg-[rgb(var(--card))] p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-semibold mb-4">{t.judicialAnalytics.title || 'Judicial Analytics'}</h2>

      <section className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div className="p-4 bg-[rgb(var(--bg))] rounded">
          <h3 className="text-sm text-[rgb(var(--muted-foreground))]">Average time to disposition (days)</h3>
          <div className="text-2xl font-bold">{data.avg_time_to_disposition_days ?? 'N/A'}</div>
        </div>
        <div className="p-4 bg-[rgb(var(--bg))] rounded">
          <h3 className="text-sm text-[rgb(var(--muted-foreground))]">Open backlog</h3>
          <div className="text-2xl font-bold">{data.backlog_size ?? 'N/A'}</div>
        </div>
        <div className="p-4 bg-[rgb(var(--bg))] rounded">
          <h3 className="text-sm text-[rgb(var(--muted-foreground))]">Cases per year (sample)</h3>
          <div className="text-lg">
            {Array.isArray(data.cases_per_year) ? (
              data.cases_per_year.slice(0,3).map((m: any, idx: number) => (
                <div key={idx}>{m.name}: <strong>{m.value}</strong></div>
              ))
            ) : 'N/A'}
          </div>
        </div>
      </section>

      <section className="mb-6">
        <h3 className="text-lg font-medium mb-2">Win rates by case type</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {Array.isArray(data.win_rates_by_case_type) ? data.win_rates_by_case_type.map((w: any, i: number) => (
            <div key={i} className="p-3 bg-[rgb(var(--bg))] rounded">
              <div className="text-sm text-[rgb(var(--muted-foreground))]">{w.name}</div>
              <div className="text-xl font-semibold">{w.value}%</div>
              {w.description && <div className="text-xs text-[rgb(var(--muted-foreground))]">{w.description}</div>}
            </div>
          )) : <div>No data</div>}
        </div>
      </section>

      <section className="mb-6">
        <h3 className="text-lg font-medium mb-2">Top insights</h3>
        <ul className="list-disc pl-5">
          {Array.isArray(data.judge_trend_insights) ? data.judge_trend_insights.map((ins: string, i: number) => (
            <li key={i}>{ins}</li>
          )) : <li>No insights</li>}
        </ul>
      </section>

      <section>
        <h3 className="text-lg font-medium mb-2">Recommended actions</h3>
        <ol className="list-decimal pl-5">
          {Array.isArray(data.recommended_resource_actions) ? data.recommended_resource_actions.map((a: string, i: number) => (
            <li key={i}>{a}</li>
          )) : <li>No recommendations</li>}
        </ol>
      </section>
    </div>
  );
};
