import { useEffect, useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { getFirestore, collection, getDocs, query, orderBy, doc, getDoc, setDoc, increment } from 'firebase/firestore';

const ADMIN_EMAIL = 'henuosr@gmail.com'; // Change to your admin email

const Admin = () => {
  const { user } = useAuth();
  const [applications, setApplications] = useState<any[]>([]);
  const [downloads, setDownloads] = useState<any[]>([]);
  const [visitorCount, setVisitorCount] = useState<number>(0);
  const [loading, setLoading] = useState(true);

  // Fetch all team applications
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const db = getFirestore();
      // Team applications
      const appsSnap = await getDocs(query(collection(db, 'team_applications'), orderBy('submittedAt', 'desc')));
      setApplications(appsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() })));
      // Downloads
      const downloadsSnap = await getDocs(query(collection(db, 'downloads'), orderBy('timestamp', 'desc')));
      setDownloads(downloadsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() })));
      // Visitor counter
      const counterRef = doc(db, 'meta', 'visitorCounter');
      const counterSnap = await getDoc(counterRef);
      setVisitorCount(counterSnap.exists() ? counterSnap.data().count : 0);
      setLoading(false);
    };
    if (user && user.email === ADMIN_EMAIL) fetchData();
  }, [user]);

  // Show login or unauthorized message
  if (!user) {
    return <div className="min-h-screen flex items-center justify-center text-2xl text-gray-700">Please sign in as admin to view this page.</div>;
  }
  if (user.email !== ADMIN_EMAIL) {
    return <div className="min-h-screen flex items-center justify-center text-2xl text-red-600">Unauthorized: Admin access only.</div>;
  }

        return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-purple-900 p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 text-center text-purple-300">Admin Dashboard</h1>
        {loading ? (
          <div className="text-center text-lg text-gray-400">Loading...</div>
        ) : (
          <>
            <div className="mb-10 p-6 bg-gray-800/60 rounded-xl shadow-lg text-white flex flex-col md:flex-row md:justify-between md:items-center">
              <div className="text-2xl font-semibold">Visitor Count: <span className="text-pink-400">{visitorCount}</span></div>
              <button
                className="mt-4 md:mt-0 px-6 py-2 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-full font-semibold shadow hover:from-purple-700 hover:to-pink-700 transition-all duration-300"
                onClick={async () => {
                  const db = getFirestore();
                  const counterRef = doc(db, 'meta', 'visitorCounter');
                  await setDoc(counterRef, { count: increment(1) }, { merge: true });
                  const counterSnap = await getDoc(counterRef);
                  setVisitorCount(counterSnap.exists() ? counterSnap.data().count : 0);
                }}
              >Increment Counter (Test)</button>
            </div>
            <div className="mb-12">
              <h2 className="text-2xl font-bold mb-4 text-purple-200">Team Applications</h2>
              <div className="overflow-x-auto">
                <table className="min-w-full bg-gray-900/80 rounded-xl">
                  <thead>
                    <tr className="text-purple-300 text-left">
                      <th className="p-2">Name</th>
                      <th className="p-2">Email</th>
                      <th className="p-2">Phone</th>
                      <th className="p-2">Address</th>
                      <th className="p-2">Skills</th>
                      <th className="p-2">Photo</th>
                      <th className="p-2">Resume</th>
                      <th className="p-2">Submitted At</th>
                    </tr>
                  </thead>
                  <tbody>
                    {applications.map(app => (
                      <tr key={app.id} className="border-b border-gray-700 hover:bg-gray-800/60">
                        <td className="p-2">{app.name}</td>
                        <td className="p-2">{app.email}</td>
                        <td className="p-2">{app.phone}</td>
                        <td className="p-2">{app.address}</td>
                        <td className="p-2">{Array.isArray(app.skills) ? app.skills.join(', ') : app.skills}</td>
                        <td className="p-2">
                          {app.photoURL ? <a href={app.photoURL} target="_blank" rel="noopener noreferrer" className="text-blue-400 underline">View</a> : '—'}
                        </td>
                        <td className="p-2">
                          {app.resumeURL ? <a href={app.resumeURL} target="_blank" rel="noopener noreferrer" className="text-blue-400 underline">View</a> : '—'}
                        </td>
                        <td className="p-2">{app.submittedAt ? new Date(app.submittedAt).toLocaleString() : ''}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
            <div>
              <h2 className="text-2xl font-bold mb-4 text-purple-200">ISO Download Records</h2>
              <div className="overflow-x-auto">
                <table className="min-w-full bg-gray-900/80 rounded-xl">
                  <thead>
                    <tr className="text-pink-300 text-left">
                      <th className="p-2">User ID</th>
                      <th className="p-2">Timestamp</th>
                      <th className="p-2">User Agent</th>
                      <th className="p-2">IP</th>
                    </tr>
                  </thead>
                  <tbody>
                    {downloads.map(dl => (
                      <tr key={dl.id} className="border-b border-gray-700 hover:bg-gray-800/60">
                        <td className="p-2">{dl.uid}</td>
                        <td className="p-2">{dl.timestamp && dl.timestamp.toDate ? dl.timestamp.toDate().toLocaleString() : (dl.timestamp ? new Date(dl.timestamp).toLocaleString() : '')}</td>
                        <td className="p-2 max-w-xs truncate">{dl.userAgent}</td>
                        <td className="p-2">{dl.ip}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default Admin;
