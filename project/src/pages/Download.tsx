import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  Download, 
  HardDrive, 
  Cpu, 
  Monitor, 
  Wifi, 
  Shield,
  ChevronDown,
  Copy,
  ExternalLink,
  FileText,
  CheckCircle,
  LogIn,
  AlertCircle,
  User,
  Crown
} from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import Login from '../components/Login';

const DownloadPage = () => {
  const [showChecksums, setShowChecksums] = useState(false);
  const [copiedChecksum, setCopiedChecksum] = useState('');
  const [showLogin, setShowLogin] = useState(false);
  const [downloadStatus, setDownloadStatus] = useState<{
    canDownload: boolean;
    remainingDownloads: number;
    error?: string;
  } | null>(null);
  const [isDownloading, setIsDownloading] = useState(false);
  
  const { user, userData, checkDownloadLimit, recordDownload } = useAuth();

  // Check download limit when user changes
  useEffect(() => {
    const checkLimit = async () => {
      if (user) {
        const status = await checkDownloadLimit();
        setDownloadStatus(status);
      } else {
        setDownloadStatus(null);
      }
    };
    
    checkLimit();
  }, [user, checkDownloadLimit]);

  // Handle download with authentication and limits
  const handleDownload = async () => {
    const url = 'https://drive.google.com/file/d/1_qA5yiDP0l0nYQRA6qlPxBuAMD7rl0rL/view?usp=sharing';
    if (!user) {
      setShowLogin(true);
      return;
    }

    if (!downloadStatus?.canDownload) {
      return;
    }

    setIsDownloading(true);
    try {
      // Record the download first
      const recordResult = await recordDownload();
      if (recordResult.success) {
        // Update download status
        const newStatus = await checkDownloadLimit();
        setDownloadStatus(newStatus);
        // Open download link (view link, not direct download)
        window.open(url, '_blank');
      } else {
        console.error('Failed to record download:', recordResult.error);
      }
    } catch (error) {
      console.error('Download error:', error);
    } finally {
      setIsDownloading(false);
    }
  };

  // Update download links to use the new Google Drive link
  const downloadMirrors = [
    {
      name: 'Google Drive (Primary)',
      url: 'https://drive.google.com/uc?export=download&id=1_qA5yiDP0l0nYQRA6qlPxBuAMD7rl0rL',
      location: 'Google Drive',
      speed: 'Fast',
      recommended: true
    },
    {
      name: 'GitHub Releases',
      url: 'https://github.com/henu-os/releases/latest',
      location: 'GitHub',
      speed: 'Good',
      recommended: false
    },
    {
      name: 'European Mirror',
      url: 'https://eu.releases.henu-os.org/latest/henu-os-2.0.iso',
      location: 'Europe',
      speed: 'Fast',
      recommended: false
    }
  ];

  const checksums = {
    md5: 'a1b2c3d4e5f6789012345678901234567890abcd',
    sha256: '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef12'
  };

  const systemRequirements = [
    {
      icon: <Cpu className="w-6 h-6" />,
      label: 'Processor',
      minimum: '64-bit x86 processor',
      recommended: 'Multi-core 2GHz+'
    },
    {
      icon: <HardDrive className="w-6 h-6" />,
      label: 'Memory',
      minimum: '2 GB RAM',
      recommended: '4 GB RAM or more'
    },
    {
      icon: <Monitor className="w-6 h-6" />,
      label: 'Storage',
      minimum: '20 GB free space',
      recommended: '50 GB SSD storage'
    },
    {
      icon: <Wifi className="w-6 h-6" />,
      label: 'Graphics',
      minimum: 'Integrated graphics',
      recommended: 'Dedicated GPU'
    }
  ];

  const installationSteps = [
    {
      step: 1,
      title: 'Download ISO',
      description: 'Download the HENU OS ISO file from one of our mirrors'
    },
    {
      step: 2,
      title: 'Create Bootable USB',
      description: 'Use Rufus (Windows) or Etcher (Linux/Mac) to create installation media'
    },
    {
      step: 3,
      title: 'Boot & Install',
      description: 'Boot from USB and follow the guided installation process'
    },
    {
      step: 4,
      title: 'Enjoy HENU OS',
      description: 'Experience voice-powered Linux with multi-language support'
    }
  ];

  const copyToClipboard = (text: string, type: string) => {
    navigator.clipboard.writeText(text);
    setCopiedChecksum(type);
    setTimeout(() => setCopiedChecksum(''), 2000);
  };

  return (
    <div className="min-h-screen pt-24 pb-16 px-6">
      <div className="container mx-auto">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h1 className="text-5xl md:text-7xl font-heading font-bold mb-8 bg-gradient-to-r from-purple-400 via-pink-400 to-orange-400 bg-clip-text text-transparent">
            Download
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 max-w-4xl mx-auto font-body leading-relaxed">
            Get the latest version of HENU OS. Choose from multiple download mirrors 
            and verify your download with checksums.
          </p>
        </motion.div>

        {/* Main Download Section */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="mb-16"
        >
          <div className="text-center mb-12">
            <div className="inline-flex items-center space-x-4 p-4 bg-gradient-to-r from-purple-900/30 to-pink-900/30 backdrop-blur-sm rounded-2xl border border-purple-400/30 mb-8">
              <Shield className="w-8 h-8 text-green-400" />
              <div className="text-left">
                <h2 className="text-2xl font-heading font-bold text-white">
                  HENU OS 2.0 LTS
                </h2>
                <p className="text-gray-300 font-body">
                  Latest stable release • 2.8 GB • Released January 2024
                </p>
              </div>
            </div>

            {/* Primary Download Button */}
            {user ? (
              <div className="space-y-4">
                {downloadStatus?.error && (
                  <div className="p-4 bg-red-900/50 border border-red-500/30 rounded-lg flex items-center space-x-2">
                    <AlertCircle className="w-5 h-5 text-red-400" />
                    <span className="text-red-300 text-sm">{downloadStatus.error}</span>
                  </div>
                )}
                
                {downloadStatus && !downloadStatus.error && (
                  <div className="p-4 bg-blue-900/50 border border-blue-500/30 rounded-lg flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <User className="w-5 h-5 text-blue-400" />
                      <span className="text-blue-300 text-sm">
                        {userData?.role === 'premium' ? (
                          <>
                            <Crown className="w-4 h-4 inline mr-1" />
                            Premium User
                          </>
                        ) : (
                          'Free User'
                        )}
                      </span>
                    </div>
                    <span className="text-blue-300 text-sm">
                      {downloadStatus.remainingDownloads} downloads remaining today
                    </span>
                  </div>
                )}

                <motion.button
                  onClick={handleDownload}
                  disabled={!downloadStatus?.canDownload || isDownloading}
                  whileHover={{ scale: downloadStatus?.canDownload ? 1.05 : 1 }}
                  className={`px-8 py-3 rounded-full font-semibold flex items-center justify-center space-x-2 transition-all duration-300 ${
                    downloadStatus?.canDownload && !isDownloading
                      ? 'bg-gradient-to-r from-purple-600 to-pink-600 text-white'
                      : 'bg-gray-600 text-gray-300 cursor-not-allowed'
                  }`}
                >
                  <Download size={20} />
                  <span>{isDownloading ? 'Opening Link...' : 'Open Download Link'}</span>
                </motion.button>
              </div>
            ) : (
              <motion.button
                onClick={() => setShowLogin(true)}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="inline-flex items-center space-x-3 px-12 py-6 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-bold text-xl rounded-full transition-all duration-300 shadow-2xl hover:shadow-purple-500/30"
              >
                <LogIn size={24} />
                <span>Sign In to Access Download</span>
              </motion.button>
            )}

            <p className="text-gray-400 font-body mt-4">
              {user ? 'Download tracked per user account' : 'Sign in required to download'}
            </p>
          </div>

          {/* Download Mirrors */}
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {downloadMirrors.map((mirror, index) => (
              <motion.button
                key={index}
                onClick={() => handleDownload(mirror.url)}
                disabled={!user || !downloadStatus?.canDownload}
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                whileHover={{ y: user && downloadStatus?.canDownload ? -5 : 0, scale: user && downloadStatus?.canDownload ? 1.02 : 1 }}
                className={`group block p-6 bg-gradient-to-br from-gray-900/50 to-black/50 backdrop-blur-sm rounded-2xl border transition-all duration-500 shadow-xl hover:shadow-2xl ${
                  mirror.recommended 
                    ? 'border-purple-400/60 hover:border-purple-400/80 shadow-purple-500/20' 
                    : 'border-purple-400/30 hover:border-purple-400/60 hover:shadow-purple-500/20'
                } ${!user || !downloadStatus?.canDownload ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}`}
              >
                {mirror.recommended && (
                  <div className="flex justify-center mb-3">
                    <span className="px-3 py-1 bg-gradient-to-r from-green-500 to-emerald-500 text-white text-xs font-semibold rounded-full">
                      Recommended
                    </span>
                  </div>
                )}
                
                <div className="text-center">
                  <ExternalLink className="w-8 h-8 text-purple-400 mx-auto mb-3 group-hover:scale-110 transition-transform duration-300" />
                  <h3 className="text-lg font-heading font-semibold text-white mb-2 group-hover:text-purple-300 transition-colors duration-300">
                    {mirror.name}
                  </h3>
                  <p className="text-gray-300 font-body text-sm mb-2">
                    {mirror.location}
                  </p>
                  <span className={`inline-block px-3 py-1 text-xs font-semibold rounded-full ${
                    mirror.speed === 'Fast' 
                      ? 'bg-green-500/20 text-green-400' 
                      : mirror.speed === 'Good'
                      ? 'bg-yellow-500/20 text-yellow-400'
                      : 'bg-orange-500/20 text-orange-400'
                  }`}>
                    {mirror.speed}
                  </span>
                </div>
              </motion.button>
            ))}
          </div>
        </motion.div>

        {/* Checksums Section */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          className="mb-16"
        >
          <div className="p-8 bg-gradient-to-br from-gray-900/30 to-black/30 backdrop-blur-sm rounded-2xl border border-purple-400/30">
            <button
              onClick={() => setShowChecksums(!showChecksums)}
              className="flex items-center justify-between w-full text-left"
            >
              <h3 className="text-2xl font-heading font-semibold text-white">
                Verify Download (Checksums)
              </h3>
              <ChevronDown 
                className={`w-6 h-6 text-purple-400 transition-transform duration-300 ${
                  showChecksums ? 'rotate-180' : ''
                }`} 
              />
            </button>
            
            <motion.div
              initial={false}
              animate={{ height: showChecksums ? 'auto' : 0, opacity: showChecksums ? 1 : 0 }}
              className="overflow-hidden"
            >
              <div className="pt-6 space-y-4">
                <p className="text-gray-300 font-body mb-6">
                  Verify the integrity of your download using these checksums:
                </p>
                
                <div className="space-y-4">
                  {Object.entries(checksums).map(([type, hash]) => (
                    <div
                      key={type}
                      className="flex items-center justify-between p-4 bg-gray-800/50 rounded-xl"
                    >
                      <div>
                        <span className="text-purple-400 font-semibold uppercase text-sm">
                          {type}:
                        </span>
                        <code className="text-gray-300 font-mono text-sm ml-2 break-all">
                          {hash}
                        </code>
                      </div>
                      <motion.button
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => copyToClipboard(hash, type)}
                        className="p-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg transition-colors duration-200"
                      >
                        {copiedChecksum === type ? (
                          <CheckCircle size={20} />
                        ) : (
                          <Copy size={20} />
                        )}
                      </motion.button>
                    </div>
                  ))}
                </div>
              </div>
            </motion.div>
          </div>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-12">
          {/* System Requirements */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            <h3 className="text-3xl font-heading font-bold text-white mb-8">
              System Requirements
            </h3>
            
            <div className="space-y-6">
              {systemRequirements.map((req, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 30 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: index * 0.1 }}
                  className="p-6 bg-gradient-to-br from-gray-900/50 to-black/50 backdrop-blur-sm rounded-2xl border border-purple-400/30"
                >
                  <div className="flex items-center space-x-4 mb-4">
                    <div className="text-purple-400">
                      {req.icon}
                    </div>
                    <h4 className="text-lg font-heading font-semibold text-white">
                      {req.label}
                    </h4>
                  </div>
                  <div className="space-y-2">
                    <div>
                      <span className="text-gray-400 text-sm">Minimum: </span>
                      <span className="text-gray-200 font-body">{req.minimum}</span>
                    </div>
                    <div>
                      <span className="text-gray-400 text-sm">Recommended: </span>
                      <span className="text-gray-200 font-body">{req.recommended}</span>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>

          {/* Installation Steps */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.5 }}
          >
            <h3 className="text-3xl font-heading font-bold text-white mb-8">
              Installation Steps
            </h3>
            
            <div className="space-y-6">
              {installationSteps.map((step, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 30 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: index * 0.1 }}
                  className="flex items-start space-x-4"
                >
                  <div className="flex-shrink-0 w-12 h-12 bg-gradient-to-br from-purple-600 to-pink-600 rounded-full flex items-center justify-center text-white font-bold text-lg">
                    {step.step}
                  </div>
                  <div className="pt-2">
                    <h4 className="text-lg font-heading font-semibold text-white mb-2">
                      {step.title}
                    </h4>
                    <p className="text-gray-300 font-body">
                      {step.description}
                    </p>
                  </div>
                </motion.div>
              ))}
            </div>

            {/* Quick Links */}
            <div className="mt-8 p-6 bg-gradient-to-br from-purple-900/30 to-pink-900/30 backdrop-blur-sm rounded-2xl border border-purple-400/30">
              <h4 className="text-lg font-heading font-semibold text-white mb-4">
                Need Help?
              </h4>
              <div className="space-y-3">
                <a
                  href="/documentation"
                  className="flex items-center space-x-2 text-purple-400 hover:text-purple-300 transition-colors duration-200"
                >
                  <FileText size={16} />
                  <span className="font-body">Installation Guide</span>
                </a>
                <a
                  href="/community"
                  className="flex items-center space-x-2 text-purple-400 hover:text-purple-300 transition-colors duration-200"
                >
                  <ExternalLink size={16} />
                  <span className="font-body">Community Support</span>
                </a>
                <a
                  href="#"
                  className="flex items-center space-x-2 text-purple-400 hover:text-purple-300 transition-colors duration-200"
                >
                  <Download size={16} />
                  <span className="font-body">PDF Manual</span>
                </a>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Call to Action */}
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mt-20"
        >
          <div className="p-12 bg-gradient-to-br from-purple-900/30 to-pink-900/30 backdrop-blur-sm rounded-3xl border border-purple-400/30 max-w-4xl mx-auto">
            <h2 className="text-4xl font-heading font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
              Ready to Get Started?
            </h2>
            <p className="text-xl text-gray-300 mb-8 font-body">
              Join thousands of developers who have made the switch to voice-powered Linux.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              {user ? (
                <motion.button
                  onClick={handleDownload}
                  disabled={!downloadStatus?.canDownload || isDownloading}
                  whileHover={{ scale: downloadStatus?.canDownload ? 1.05 : 1 }}
                  className={`px-8 py-3 rounded-full font-semibold flex items-center justify-center space-x-2 transition-all duration-300 ${
                    downloadStatus?.canDownload && !isDownloading
                      ? 'bg-gradient-to-r from-purple-600 to-pink-600 text-white'
                      : 'bg-gray-600 text-gray-300 cursor-not-allowed'
                  }`}
                >
                  <Download size={20} />
                  <span>{isDownloading ? 'Opening Link...' : 'Open Download Link'}</span>
                </motion.button>
              ) : (
                <motion.button
                  onClick={() => setShowLogin(true)}
                  whileHover={{ scale: 1.05 }}
                  className="px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-full font-semibold flex items-center justify-center space-x-2 transition-all duration-300"
                >
                  <LogIn size={20} />
                  <span>Sign In to Access Download</span>
                </motion.button>
              )}
              <motion.a
                href="/documentation"
                whileHover={{ scale: 1.05 }}
                className="px-8 py-3 border-2 border-purple-400 text-purple-400 hover:bg-purple-400 hover:text-black rounded-full font-semibold flex items-center justify-center space-x-2 transition-all duration-300"
              >
                <FileText size={20} />
                <span>Read Docs</span>
              </motion.a>
            </div>
          </div>
        </motion.div>
      </div>
      
      {/* Login Modal */}
      {showLogin && (
        <Login onClose={() => setShowLogin(false)} />
      )}
    </div>
  );
};

export default DownloadPage;